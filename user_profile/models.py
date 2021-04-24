from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class UserProfile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile', blank=True)

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    location = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)

    friends_with = models.ManyToManyField(to='self', related_name='befriended_by', blank=True)
    following = models.ManyToManyField(to='self', related_name='followers', blank=True, symmetrical=False)

    def __str__(self):
        return f'#{self.id} - {self.user.username} ({self.user.email})'
