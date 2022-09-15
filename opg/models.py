from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(max_length=20)
    opg = models.TextField(max_length=20)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance)
    instance.owner.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


