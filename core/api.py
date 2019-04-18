from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Human, Sibling, Child, Avatar, Parent
from .serializer import UserSerializer, HumanSerializer, ParentSerializer, SiblingSerializer, ChildSerializer, \
    AvatarSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return super(UserViewSet, self).get_permissions()


class HumanViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all man objects.

    create:
    Create a new man instance.
    """
    queryset = Human.objects.all()
    serializer_class = HumanSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class SiblingViewSet(viewsets.ModelViewSet):
    queryset = Sibling.objects.all()
    serializer_class = SiblingSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer