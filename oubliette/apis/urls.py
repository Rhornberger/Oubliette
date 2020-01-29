from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, SpellViewSet, ProfileViewSet #User View sets and spell view sets


# from references import views
from . import views

# this is reregistering the different routers for the viewsets
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('spell', SpellViewSet, basename='spell')
router.register('character', ProfileViewSet, basename='character')
router.register('craft', ProfileViewSet, basename='craft')
router.register('knowledge', ProfileViewSet, basename='knowledge')
router.register('perform', ProfileViewSet, basename='perform')
router.register('profession', ProfileViewSet, basename='profession')
router.register('language', ProfileViewSet, basename='language')
router.register('weapon', ProfileViewSet, basename='weapon')
router.register('ac_item', ProfileViewSet, basename='ac_item')
router.register('gear', ProfileViewSet, basename='gear')
router.register('feat', ProfileViewSet, basename='feat')
router.register('special_ability', ProfileViewSet, basename='special_ability')
router.register('zero_lvl_spell', ProfileViewSet, basename='zero_lvl_spell')
router.register('first_lvl_spell', ProfileViewSet, basename='first_lvl_spell')
router.register('second_lvl_spell', ProfileViewSet, basename='second_lvl_spell')
router.register('third_lvl_spell', ProfileViewSet, basename='third_lvl_spell')
router.register('fourth_lvl_spell', ProfileViewSet, basename='fourth_lvl_spell')
router.register('fifth_lvl_spell', ProfileViewSet, basename='fifth_lvl_spell')
router.register('sixth_lvl_spell', ProfileViewSet, basename='sixth_lvl_spell')
router.register('seventh_lvl_spell', ProfileViewSet, basename='seventh_lvl_spell')
router.register('eighth_lvl_spell', ProfileViewSet, basename='eighth_lvl_spell')
router.register('ninth_lvl_spell', ProfileViewSet, basename='ninth_lvl_spell')
# router.register('', CharacterViewSet, basename='characters')

urlpatterns = router.urls
# urlpatterns = [
#     path('spell', views.SpellAPIView.as_view())
# ]