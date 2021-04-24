from django.contrib.auth import get_user_model
from django.db import models

from user.models import User
from user_profile.models import UserProfile


class Post(models.Model):
    content = models.TextField()

    posted_by = models.ForeignKey(to=UserProfile, on_delete=models.SET_NULL, related_name='posts', null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    liked_by = models.ManyToManyField(to=UserProfile, related_name='liked_posts', blank=True)

    shared_post = models.ForeignKey(to='self', on_delete=models.SET_NULL, related_name='shared_in_posts', blank=True, null=True)

    def __str__(self):
        if self.posted_by:
            return f'Post #{self.id} by {self.posted_by.user.username} on ' \
                   f'{"{:02d}".format(self.created.year)}/' \
                   f'{"{:02d}".format(self.created.month)}/' \
                   f'{"{:02d}".format(self.created.day)} ' \
                   f'at {"{:02d}".format(self.created.hour)}:{"{:02d}".format(self.created.minute)}'
        else:
            return f'Post #{self.id} by deleted user on ' \
                   f'{"{:02d}".format(self.created.year)}/' \
                   f'{"{:02d}".format(self.created.month)}/' \
                   f'{"{:02d}".format(self.created.day)} ' \
                   f'at {"{:02d}".format(self.created.hour)}:{"{:02d}".format(self.created.minute)}'
