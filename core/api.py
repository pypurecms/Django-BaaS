from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from core.models import Human
from core.serializer import UserSerializer, HumanSerializer

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


class ManViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all man objects.

    create:
    Create a new man instance.
    """
    queryset = Human.objects.all()
    serializer_class = HumanSerializer