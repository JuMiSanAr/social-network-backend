
from rest_framework import serializers

from comment.serializers.CommentsInPost import CommentsInPostSerializer
from image.serializer import ImageSerializer
from post.models import Post
from post.serializers.nested_basic import BasicPostNestedSerializer
from user_profile.serializers.nested import UserProfileNestedSerializer


class PostNestedSerializer(serializers.ModelSerializer):

    shared_post = BasicPostNestedSerializer(read_only=True)
    liked_by = UserProfileNestedSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    comments = CommentsInPostSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id',
                  'content',
                  'created',
                  'last_updated',
                  'shared_post',
                  'liked_by',
                  'images',
                  'comments']

        read_only_fields = ['shared_post', 'liked_by', 'images', 'comments']

        ordering = ['created']
