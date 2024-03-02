import datetime
from django.db.models import Count
from rest_framework.generics import ListAPIView, UpdateAPIView
from core.models import Product, Group
from core.api_v1.serializers import ProductInfoSerializer, GroupSerializer
from core.api_v1.serializers import AddUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from core.common import distribute_pupiles_in_groups
from rest_framework.views import APIView


class ProductAPIView(ListAPIView):
    serializer_class = ProductInfoSerializer
 
    def get_queryset(self):
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
