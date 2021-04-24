from rest_framework import serializers

from friend_request.Serializers.default import FriendRequestSerializer
from friend_request.Serializers.received_by_serializer import FriendRequestReceivedBySerializer
from friend_request.Serializers.sent_by_serializer import FriendRequestSentBySerializer
from post.serializers.nested import PostNestedSerializer
from user_profile.models import UserProfile
from user_profile.serializers.nested import UserProfileNestedSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    friends_with = UserProfileNestedSerializer(many=True)
    following = UserProfileNestedSerializer(many=True)
    followers = UserProfileNestedSerializer(many=True)

    received_friend_requests = FriendRequestSentBySerializer(many=True)
    sent_friend_requests = FriendRequestReceivedBySerializer(many=True)

    posts = PostNestedSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['id',
                  'avatar',
                  'location',
                  'phone',
                  'about',
                  'hobbies',
                  'posts',
                  'friends_with',
                  'received_friend_requests',
                  'sent_friend_requests',
                  'following',
                  'followers']
