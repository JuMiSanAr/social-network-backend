from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from post.models import Post
from user_profile.models import UserProfile


class Comment(models.Model):

    content = models.TextField(blank=True)

    user = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, related_name='comments', null=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, default=0, related_name='comments')
