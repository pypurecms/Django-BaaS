from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Human, Sibling, Child, Avatar, Parent
from .serializer import UserSerializer, HumanSerializer, ParentSerializer, SiblingSerializer, ChildSerializer, \
    AvatarSerializer
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list']:
            return [IsAdminUser()]
        elif self.action in ['read']:
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'delete']:
            return [IsAuthenticated(), IsOwner()]
        return super(UserViewSet, self).get_permissions()



class HumanViewSet(viewsets.ModelViewSet):
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
