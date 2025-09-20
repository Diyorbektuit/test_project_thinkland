from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry
from .models import Product

@receiver(post_save, sender=Product)
def index_product(sender, instance, **kwargs):
    registry.update(instance)

@receiver(post_delete, sender=Product)
def delete_product(sender, instance, **kwargs):
    registry.delete(instance)
