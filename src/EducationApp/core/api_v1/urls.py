from django.urls import path
from core.api_v1.views import (
    ProductAPIView,
    LessonAPIView,
    AddUserInProductAPIView,
    DistributeUsersAPIView,
)

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name="get-available_products-api"),
    path(
        'products/<int:product_id>/<int:user_id>',
        LessonAPIView.as_view(),
        name="get-available-product-lessons-api"
    ),
    path(
        'products/<int:product_id>/add_member',
        AddUserInProductAPIView.as_view(),
        name="add-user-to-product-api"
    ),
    path(
        'products/<int:product_id>/distribute_members',
        DistributeUsersAPIView.as_view(),
        name="distribute-members-api"
    ),
]
