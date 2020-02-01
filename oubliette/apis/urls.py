from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, SpellViewSet, ProfileViewSet, CharacterViewSet, CraftViewSet, KnowledgeViewSet, PerformViewSet, ProfessionViewSet, LanguageViewSet, WeaponViewSet, Ac_ItemViewSet, GearViewSet, FeatViewSet, Special_AbilityViewSet, Zero_Lvl_SpellViewSet, First_Lvl_SpellViewSet, Second_Lvl_SpellViewSet, Third_Lvl_SpellViewSet, Fourth_Lvl_SpellViewSet, Fifth_Lvl_SpellViewSet, Sixth_Lvl_SpellViewSet, Seventh_Lvl_SpellViewSet, Eighth_Lvl_SpellViewSet, Ninth_Lvl_SpellViewSet, NoteViewSet, RaceViewSet #User View sets and spell view sets


# from references import views
from . import views

# this is reregistering the different routers for the viewsets
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('spell', SpellViewSet, basename='spell')
router.register('profile', ProfileViewSet, basename='profile')
router.register('character', CharacterViewSet, basename='character')
router.register('craft', CraftViewSet, basename='craft')
router.register('knowledge', KnowledgeViewSet, basename='knowledge')
router.register('perform', PerformViewSet, basename='perform')
router.register('profession', ProfessionViewSet, basename='profession')
router.register('language', LanguageViewSet, basename='language')
router.register('weapon', WeaponViewSet, basename='weapon')
router.register('ac_item', Ac_ItemViewSet, basename='ac_item')
router.register('gear', GearViewSet, basename='gear')
router.register('feat', FeatViewSet, basename='feat')
router.register('special_ability', Special_AbilityViewSet, basename='special_ability')
router.register('zero_lvl_spell', Zero_Lvl_SpellViewSet, basename='zero_lvl_spell')
router.register('first_lvl_spell', First_Lvl_SpellViewSet, basename='first_lvl_spell')
router.register('second_lvl_spell', Second_Lvl_SpellViewSet, basename='second_lvl_spell')
router.register('third_lvl_spell', Third_Lvl_SpellViewSet, basename='third_lvl_spell')
router.register('fourth_lvl_spell', Fourth_Lvl_SpellViewSet, basename='fourth_lvl_spell')
router.register('fifth_lvl_spell', Fifth_Lvl_SpellViewSet, basename='fifth_lvl_spell')
router.register('sixth_lvl_spell', Sixth_Lvl_SpellViewSet, basename='sixth_lvl_spell')
router.register('seventh_lvl_spell', Seventh_Lvl_SpellViewSet, basename='seventh_lvl_spell')
router.register('eighth_lvl_spell', Eighth_Lvl_SpellViewSet, basename='eighth_lvl_spell')
router.register('ninth_lvl_spell', Ninth_Lvl_SpellViewSet, basename='ninth_lvl_spell')
router.register('note', NoteViewSet, basename='note')
router.register('race', RaceViewSet, basename='race')


urlpatterns = router.urls
# urlpatterns = [
#     path('spell', views.SpellAPIView.as_view())
# ]