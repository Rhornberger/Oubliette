from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, SpellViewSet, ProfileViewSet #User View sets and spell view sets


# from references import views
from . import views

# this is reregistering the different routers for the viewsets
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('spell', SpellViewSet, basename='spell')
router.register('profile', ProfileViewSet, basename='profile')
# router.register('', CharacterViewSet, basename='characters')

urlpatterns = router.urls
# urlpatterns = [
#     path('spell', views.SpellAPIView.as_view())
# ]