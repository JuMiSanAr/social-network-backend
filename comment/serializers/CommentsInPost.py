from rest_framework import serializers

from comment.models import Comment
from user_profile.serializers.nested import UserProfileNestedSerializer


class CommentsInPostSerializer(serializers.ModelSerializer):

    user = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'user']

    read_only_fields = ['user']
