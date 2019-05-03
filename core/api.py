from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Human, Sibling, Child, Avatar, Parent
from .serializer import UserSerializer, HumanSerializer, ParentSerializer, SiblingSerializer, ChildSerializer, \
    AvatarSerializer
from .permissions import IsOwner, IsOwnerOrAdmin


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



class TheModelViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['list']:
            return [IsAdminUser()]
        elif self.action in ['list_mine', 'create']:
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'delete']:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return super(TheModelViewSet, self).get_permissions()


    @action(detail=False, methods=['GET'])
    def list_mine(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user=self.request.user)
        return super(TheModelViewSet, self).list(request, args, kwargs)

class HumanViewSet(TheModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer



class ParentViewSet(TheModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer



class SiblingViewSet(TheModelViewSet):
    queryset = Sibling.objects.all()
    serializer_class = SiblingSerializer


class ChildViewSet(TheModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class AvatarViewSet(TheModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
