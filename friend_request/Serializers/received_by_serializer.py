from rest_framework import serializers
from friend_request.models import FriendRequest
from user_profile.serializers.nested import UserProfileNestedSerializer


class FriendRequestReceivedBySerializer(serializers.ModelSerializer):

    received_by = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id',
                  'status',
                  'received_by',
                  'resolved_time']

        read_only_fields = ['received_by']