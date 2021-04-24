from rest_framework import serializers
from registration.models import Registration
from user_profile.serializers.nested import UserProfileNestedSerializer


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ['id', 'used', 'code', 'action']
        read_only_fields = ['code']


