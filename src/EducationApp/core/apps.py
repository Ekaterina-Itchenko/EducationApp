from django.apps import AppConfig
from django.db.models.signals import m2m_changed


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from core.signals import user_saved_as_available
        from core.models import Product

        m2m_changed.connect(user_saved_as_available, sender=Product.pupiles.through)


