from core.models import Lesson, Product
from core.api_v1.serializers import LessonInfoSerializer
from rest_framework import views
from rest_framework.response import Response


class LessonAPIView(views.APIView):
    
    def get(self, request, product_id, user_id, format=None):
        query_result = (
            Lesson.objects
            .select_related("product")
            .prefetch_related("product__pupiles")
            .filter(
                product__pupiles__pupiles=user_id,
                product__pupiles__available_products=product_id
            )
        )
        lessons_serializer = LessonInfoSerializer(query_result, many=True)

        return Response(data=lessons_serializer.data)
