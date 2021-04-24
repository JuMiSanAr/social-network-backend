from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Post
from user_profile.serializers.nested import UserProfileNestedSerializer


class BasicPostNestedSerializer(serializers.ModelSerializer):

    posted_by = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id',
                  'content',
                  'posted_by',
                  'created']

        read_only_fields = ['posted_by']

        ordering = ['created']
