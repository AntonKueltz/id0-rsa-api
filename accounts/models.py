from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from problems.models import Problem


class UserData(models.Model):
    """data associated with user"""
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    solved = models.ManyToManyField(Problem, related_name='solvers')
    email_updates = models.BooleanField(default=False)


def create_user_data(sender, instance, created, **kwargs):
    if created:
        UserData.objects.create(user=instance)


post_save.connect(create_user_data, sender=User)
