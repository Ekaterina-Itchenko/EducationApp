from core.models import Group
from django.contrib.auth import get_user_model
from django.db.models import Count

def user_saved_as_available(sender, instance, action, pk_set, **kwargs) -> None:
    if action in ("post_add",):
        selected_groups = (
            Group.objects.filter(product__id=instance.pk)
            .prefetch_related("members")
            .annotate(pupiles_number=Count("members"))
            .filter(pupiles_number__lt=instance.max_pupiles)
            .order_by("-pupiles_number")
        )

        group = selected_groups.first()
        
        if group:
            user = get_user_model().objects.get(pk=list(pk_set)[0])
            group.members.add(user)
