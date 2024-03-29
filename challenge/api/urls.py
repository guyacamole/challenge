from django.urls import path, include
from rest_framework import routers
from api import views
from .views import PropertyViewSet

router = routers.DefaultRouter()
router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]