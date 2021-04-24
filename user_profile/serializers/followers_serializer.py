from rest_framework import serializers

from user.serializers.nested import UserNestedSerializer
from user_profile.models import UserProfile
from user_profile.serializers.nested import UserProfileNestedSerializer


class UserProfileFollowersSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer()
    following = UserProfileNestedSerializer(many=True)
    followers = UserProfileNestedSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'following', 'followers']
