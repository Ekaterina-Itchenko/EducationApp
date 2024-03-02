from django.db import models
from django.contrib.auth import get_user_model


class AvailableProduct(models.Model):
    """Describes the fields and attributes of the AvailableProduct model in the database."""

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="pupiles")
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE, related_name="available_products")

    class Meta:
        """Describes class metadata."""

        db_table = "available_products"
        unique_together = [["user", "product"]]