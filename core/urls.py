from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views, api

router = routers.DefaultRouter()
router.register('users', api.UserViewSet),
router.register('humans', api.ManViewSet, basename='humans')

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title="doc")),
    path('ping', views.ping, name='ping'),
]