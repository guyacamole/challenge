from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from .views import PropertyViewSet


router = routers.DefaultRouter()
router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', api_view(['GET'])(authentication_classes([])(permission_classes([AllowAny])(PropertyViewSet))))
]
