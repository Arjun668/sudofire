from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Customer


@receiver(post_save, sender=User)
def my_handler(sender,instance, **kwargs):
    customer_list = Customer.objects.filter(user=instance)
    if not customer_list:
        Customer(user=instance).save()