from django.db import models
from django.contrib.auth import get_user_model


class GroupMember(models.Model):
    """Describes the fields and attributes of the GroupMember model in the database."""

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="group_members")
    group = models.ForeignKey(to="Group", on_delete=models.CASCADE, related_name="groups")

    class Meta:
        """Describes class metadata."""

        db_table = "group_members"
        unique_together = [["user", "group"]]
