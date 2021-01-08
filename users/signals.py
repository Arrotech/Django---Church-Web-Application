from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """[summary]

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """[summary]

    Args:
        sender ([type]): [description]
        instance ([type]): [description]
        created ([type]): [description]
    """
    instance.profile.save()