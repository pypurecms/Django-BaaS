from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrAdmin

PERMS_DICT={
    'any': False,
    'auth': IsAuthenticated,
    'owner': IsOwnerOrAdmin,
    'staff': IsAdminUser
}

def __get_model(name):
    return settings.MODEL_DICT.get(name, {})


def get_url_name(name):
    return __get_model(name).get('plural', name).lower()


def get_enabled(name):
    return __get_model(name).get('enable', False)


def get_model_name(name):
    return __get_model(name).get('name', name).capitalize()


def get_plural_name(name):
    return __get_model(name).get('plural', name).capitalize()


def __get_permissions(model_name):
    return __get_model(model_name).get('permissions', {
        'create': 'any',
        'read': 'auth',
        'update': 'staff',
        'delete': 'staff',
        'list': 'any',
        'list_mine': 'auth'
    })

def get_permission(model_name, perm):
    print(__get_permissions(model_name))
    perm =  __get_permissions(model_name).get(perm)
    if (PERMS_DICT.get(perm, IsAdminUser)):
        return PERMS_DICT.get(perm, IsAdminUser)()


