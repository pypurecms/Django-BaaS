from django.contrib.auth.models import User
from rest_framework import viewsets
from core.models import Man
from core.serializer import UserSerializer, ManSerializer

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


class ManViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all man objects.

    create:
    Create a new man instance.
    """
    queryset = Man.objects.all()
    serializer_class = ManSerializer