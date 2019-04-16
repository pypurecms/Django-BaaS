from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Man


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ManSerializer(serializers.ModelSerializer):
    class Meta:
        model = Man
        fields = ('name', 'content')