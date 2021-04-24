from rest_framework import serializers

from comment.models import Comment
from post.serializers.nested_basic import BasicPostNestedSerializer


class CommentsByUserSerializer(serializers.ModelSerializer):

    post = BasicPostNestedSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'content',
                  'post']

    read_only_fields = ['post']
