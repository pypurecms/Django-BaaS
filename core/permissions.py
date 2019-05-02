from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            if obj.id == request.user.id:
                return True
            return False
        elif obj.user == request.user:
            return True
        return False
