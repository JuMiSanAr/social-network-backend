from django.db import models

# Create your models here.
from post.models import Post


class Image(models.Model):

    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    post = models.ForeignKey(to=Post, on_delete=models.SET_NULL, related_name='images', blank=True, null=True)
