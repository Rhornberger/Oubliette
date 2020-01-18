from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet #CharacterViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
# router.register('', CharacterViewSet, basename='characters')

urlpatterns = router.urls
