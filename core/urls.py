from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views, api

router = routers.DefaultRouter()
router.register('users', api.UserViewSet),
router.register('humans', api.HumanViewSet, basename='humans')
router.register('childs', api.ChildViewSet, basename='childs')
router.register('parent', api.ParentViewSet, basename='parents')
router.register('siblings', api.SiblingViewSet, basename='siblings')
router.register('avatars', api.AvatarViewSet, basename='avatars')

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title="doc")),
    path('ping', views.ping, name='ping'),
]