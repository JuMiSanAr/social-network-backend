from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserNestedSerializer(serializers.ModelSerializer):

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
                  'is_superuser']

    ordering = ['id']
