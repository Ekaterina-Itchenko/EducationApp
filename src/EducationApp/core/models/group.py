from django.db import models
from django.contrib.auth import get_user_model


class Group(models.Model):
    """Describes the fields and attributes of the Group model in the database."""

    name = models.CharField(max_length=250)
    product = models.ForeignKey(
        to="Product",
        on_delete=models.CASCADE,
        related_name="groups"
    )
    members = models.ManyToManyField(
        to=get_user_model(),
        through="GroupMember",
        related_name="available_groups"
    )

    class Meta:
        """Describes class metadata."""

        db_table = "groups"
