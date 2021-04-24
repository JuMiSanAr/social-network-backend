from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Post
from user_profile.serializers.nested import UserProfileNestedSerializer


class PostLikesSerializer(serializers.ModelSerializer):

    liked_by = UserProfileNestedSerializer(read_only=True, many=True)
    posted_by = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id',
                  'content',
                  'posted_by',
                  'liked_by',
                  'created']

        read_only_fields = ['posted_by', 'liked_by']

        ordering = ['created']
