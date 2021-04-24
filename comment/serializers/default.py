from rest_framework import serializers

from comment.models import Comment
from post.serializers.nested_basic import BasicPostNestedSerializer
from user_profile.serializers.nested import UserProfileNestedSerializer


class CommentsDefaultSerializer(serializers.ModelSerializer):

    post = BasicPostNestedSerializer(read_only=True)
    user = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'post',
                  'user']

    read_only_fields = ['post', 'user']
