from rest_framework import serializers
from friend_request.models import FriendRequest
from user_profile.serializers.nested import UserProfileNestedSerializer


class FriendRequestSentBySerializer(serializers.ModelSerializer):

    sent_by = UserProfileNestedSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ['id',
                  'status',
                  'sent_by',
                  'resolved_time']

        read_only_fields = ['sent_by']