from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet #CharacterViewSet
from django.urls import path
from references import views

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
# router.register('spells', )
# router.register('', CharacterViewSet, basename='characters')

urlpatterns = router.urls
urlpatterns = [
    path('spell', views.SpellAPIView.as_view())
]