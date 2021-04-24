from rest_framework import serializers

from user.serializers.nested import UserNestedSerializer
from user_profile.models import UserProfile


class UserProfileNestedSerializer(serializers.ModelSerializer):

    user = UserNestedSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'avatar', 'friends_with', 'following']
