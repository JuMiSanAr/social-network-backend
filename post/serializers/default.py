from rest_framework import serializers

from comment.serializers.CommentsInPost import CommentsInPostSerializer
from image.serializer import ImageSerializer
from post.models import Post
from post.serializers.nested_basic import BasicPostNestedSerializer
from user_profile.serializers.nested import UserProfileNestedSerializer


class PostDetailedSerializer(serializers.ModelSerializer):

    shared_post = BasicPostNestedSerializer(read_only=True)
    posted_by = UserProfileNestedSerializer(read_only=True)
    liked_by = UserProfileNestedSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    comments = CommentsInPostSerializer(read_only=True, many=True)

    logged_in_user_liked = serializers.SerializerMethodField(read_only=True)
    is_from_logged_in_user = serializers.SerializerMethodField(read_only=True)

    def get_is_from_logged_in_user(self, instance):
        if instance.posted_by == self.context['request'].user.profile:
            return True
        else:
            return False

    def get_logged_in_user_liked(self, instance):
        if self.context['request'].user.profile in instance.liked_by.values():
            return True
        else:
            return False

    class Meta:
        model = Post
        fields = ['id',
                  'content',
                  'posted_by',
                  'created',
                  'last_updated',
                  'shared_post',
                  'liked_by',
                  'images',
                  'comments',
                  'logged_in_user_liked',
                  'is_from_logged_in_user']

        read_only_fields = ['posted_by', 'shared_post', 'liked_by', 'comments']
