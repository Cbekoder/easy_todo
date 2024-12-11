from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RejaViewSet

router = DefaultRouter()
router.register(r'', RejaViewSet, basename='reja')

urlpatterns = [
    path('', include(router.urls)),
]
