from django.urls import path, include
from rest_framework import routers

from . import views, api

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]