from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField
from rest_framework.authtoken.models import Token
from django.utils.text import slugify



@receiver(post_save, sender=User)
def createUserInfo(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        # UserNotification.objects.create(userModel=instance,notification_id=1)
        # UserFollow.objects.create(user=instance)
        # n = UserNotification(userModel=instance, notification=1)
        # n.save()


