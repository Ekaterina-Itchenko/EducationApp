from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    """Describes the fields and attributes of the Product model in the database."""

    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    start_date = models.DateTimeField()
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="products"
    )
    min_pupiles = models.PositiveIntegerField()
    max_pupiles = models.PositiveIntegerField()
    pupiles = models.ManyToManyField(
        to=get_user_model(),
        through="AvailableProduct",
        related_name="available_products"
    )

    class Meta:
        """Describes class metadata."""

        db_table = "products"
