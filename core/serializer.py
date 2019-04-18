from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Human, Child, Parent, Sibling, Avatar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ('id', 'user', 'name', 'content', 'data', 'childs', 'parent', 'siblings')

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'user', 'content', 'human', 'name')

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class SiblingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sibling
        fields = '__all__'

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = '__all__'