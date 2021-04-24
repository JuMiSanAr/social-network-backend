from django.db import models

# Create your models here.
from user_profile.models import UserProfile


class Registration(models.Model):
    code = models.CharField(max_length=36)

    used = models.BooleanField(default=False, blank=False)

    user = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE, related_name='code', null=True)

    action = models.CharField(choices=[('R', 'registration'), ('PR', 'password reset')], max_length=2, default='R')