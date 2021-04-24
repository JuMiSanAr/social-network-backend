from rest_framework import serializers
from friend_request.models import FriendRequest
from user_profile.serializers.nested import UserProfileNestedSerializer


class FriendRequestSerializer(serializers.ModelSerializer):

    sent_by = UserProfileNestedSerializer(read_only=True)
    received_by = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = '__all__'

        read_only_fields = ['sent_by', 'received_by']