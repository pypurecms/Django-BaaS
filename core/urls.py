from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from django.conf import settings

from . import views, api

def get_name(name):
    return settings.MODEL_DICT.get(name).lower()

router = routers.DefaultRouter()
router.register('users', api.UserViewSet),
router.register(get_name('humans'), api.HumanViewSet, basename='humans')
router.register(get_name('childs'), api.ChildViewSet, basename='childs')
router.register(get_name('parents'), api.ParentViewSet, basename='parents')
router.register(get_name('siblings'), api.SiblingViewSet, basename='siblings')
router.register(get_name('avatars'), api.AvatarViewSet, basename='avatars')

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title="doc")),
    path('ping', views.ping, name='ping'),
]
