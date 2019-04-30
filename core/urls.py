from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views, api
from .utils import get_url_name, get_enabled

router = routers.DefaultRouter()
router.register('users', api.UserViewSet),
if get_enabled('human'): router.register(get_url_name('human'), api.HumanViewSet, basename='humans')
if get_enabled('child'): router.register(get_url_name('child'), api.ChildViewSet, basename='children')
if get_enabled('parent'): router.register(get_url_name('parent'), api.ParentViewSet, basename='parents')
if get_enabled('sibling'): router.register(get_url_name('sibling'), api.SiblingViewSet, basename='siblings')
if get_enabled('avatar'): router.register(get_url_name('avatar'), api.AvatarViewSet, basename='avatars')

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title="doc")),
    path('ping', views.ping, name='ping'),
]
