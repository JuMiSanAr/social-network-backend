from django.contrib.auth import get_user_model
from rest_framework import serializers

from user_profile.serializers.default import UserProfileSerializer
from user_profile.serializers.nested import UserProfileNestedSerializer

User = get_user_model()


class UserDetailedSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'date_joined',
                  'last_login',
                  'is_staff',
                  'is_superuser',
                  'profile']
