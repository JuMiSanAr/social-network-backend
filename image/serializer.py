from django.contrib.auth import get_user_model
from rest_framework import serializers

from image.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
