from core.api_v1.serializers import ProductInfoSerializer, GroupSerializer
from core.api_v1.serializers import AddUserSerializer
from core.common import distribute_pupiles_in_groups
from core.models import Product, Group
import datetime
from django.db.models import Count
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class ProductAPIView(ListAPIView):
    serializer_class = ProductInfoSerializer
 
    def get_queryset(self):
        '''Get product common information with amount of lessons.'''

        query_result = (
        Product.objects.filter(start_date__gte=datetime.date.today())
        .select_related("author")
        .prefetch_related("lessons").annotate(amount_of_lessons=Count("lessons"))
        )
        return query_result


class AddUserInProductAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddUserSerializer

    def patch(self, request, product_id, *args, **kwargs):
        '''Get access to the product.'''

        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_id = data.get("id")
            try:
                user = get_user_model().objects.get(pk=user_id)
            except get_user_model().DoesNotExist:
                return Response(status=HTTP_400_BAD_REQUEST)
            
            pr = Product.objects.get(pk=product_id)
            pr.pupiles.add(user)      
            return Response(serializer.data)

        else:
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class DistributeUsersAPIView(APIView):
 
    def get(self, request, product_id):
        '''
        Distribution of students into groups of product.
        Return list of groups.
        '''

        groups = Group.objects.filter(product__id=product_id)
        users = (
            get_user_model().objects
            .prefetch_related("available_products")
            .filter(available_products=product_id)
        )

        distribute_pupiles_in_groups(groups=groups, users=users)

        groups = Group.objects.filter(product__id=product_id).prefetch_related("members")
        serializer = GroupSerializer(groups, many=True)

        return Response(data=serializer.data)
