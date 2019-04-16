from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views, api

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title="doc")),
    path('', views.index, name='index'),
]