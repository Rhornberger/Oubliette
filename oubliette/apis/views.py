from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt # for csrf_exempt
# from django.utils.decorators import mathod_decorator # for csrf_exempt

from characters.models import Character

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apis import serializers
from references.models import Spell, Race
from users.models import Profile
from characters.models import Character, Craft, Knowledge, Perform, Profession, Language, Weapon, Ac_Item, Gear, Feat, Special_Ability, Zero_Lvl_Spell, First_Lvl_Spell, Second_Lvl_Spell, Third_Lvl_Spell, Fourth_Lvl_Spell, Fifth_Lvl_Spell, Sixth_Lvl_Spell, Seventh_Lvl_Spell,Eighth_Lvl_Spell, Ninth_Lvl_Spell, Note
from .serializers import SpellSerializer #this will Serialize the info from the bd on spells
from .serializers import UserSerializer  #this will Serialize the info from the bd on users
from .serializers import ProfileSerializer #this will serialize the info from DB on profiles
from .serializers import CharacterSerializer, CraftSerializer, KnowledgeSerializer, PerformSerializer, ProfessionSerializer, LanguageSerializer, WeaponSerializer, Ac_ItemSerializer, GearSerializer, FeatSerializer, Special_AbilitySerializer, Zero_Lvl_SpellSerializer, First_Lvl_SpellSerializer, Second_Lvl_SpellSerializer, Third_Lvl_SpellSerializer, Fourth_Lvl_SpellSerializer, Fifth_Lvl_SpellSerializer, Sixth_Lvl_SpellSerializer, Seventh_Lvl_SpellSerializer, Eighth_Lvl_SpellSerializer, Ninth_Lvl_SpellSerializer, NoteSerializer, RaceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer

class ProfileViewSet(viewsets.ModelViewSet):
   queryset = Profile.objects.all()
   serializer_class = ProfileSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CraftViewSet(viewsets.ModelViewSet):
    queryset = Craft.objects.all()
    serializer_class = CraftSerializer

class KnowledgeViewSet(viewsets.ModelViewSet):
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer

class PerformViewSet(viewsets.ModelViewSet):
    queryset = Perform.objects.all()
    serializer_class = PerformSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

class Ac_ItemViewSet(viewsets.ModelViewSet):
    queryset = Ac_Item.objects.all()
    serializer_class = Ac_ItemSerializer

class GearViewSet(viewsets.ModelViewSet):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer

class FeatViewSet(viewsets.ModelViewSet):
    queryset = Feat.objects.all()
    serializer_class = FeatSerializer

class Special_AbilityViewSet(viewsets.ModelViewSet):
    queryset = Special_Ability.objects.all()
    serializer_class = Special_AbilitySerializer

class Zero_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Zero_Lvl_Spell.objects.all()
    serializer_class = Zero_Lvl_SpellSerializer

class First_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = First_Lvl_Spell.objects.all()
    serializer_class = First_Lvl_SpellSerializer

class Second_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Second_Lvl_Spell.objects.all()
    serializer_class = Second_Lvl_SpellSerializer

class Third_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Third_Lvl_Spell.objects.all()
    serializer_class = Third_Lvl_SpellSerializer

class Fourth_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Fourth_Lvl_Spell.objects.all()
    serializer_class = Fourth_Lvl_SpellSerializer

class Fifth_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Fifth_Lvl_Spell.objects.all()
    serializer_class = Fifth_Lvl_SpellSerializer

class Sixth_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Sixth_Lvl_Spell.objects.all()
    serializer_class = Sixth_Lvl_SpellSerializer

class Seventh_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Seventh_Lvl_Spell.objects.all()
    serializer_class = Seventh_Lvl_SpellSerializer

class Eighth_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Eighth_Lvl_Spell.objects.all()
    serializer_class = Eighth_Lvl_SpellSerializer

class Ninth_Lvl_SpellViewSet(viewsets.ModelViewSet):
    queryset = Ninth_Lvl_Spell.objects.all()
    serializer_class = Ninth_Lvl_SpellSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    
# class SpellAPIView(APIView):
#     """Test Api View"""
#     serializer_class = serializers.SpellSerializer

#     def get(self, request, format=None):
#         """Returns a list of APIView features"""
#         an_apiview = [
#             'Uses Http methods as functions (get, post, patch, put, delete)',
#             'Is similar to a traditional Django View',
#             'Gives you the most control over your application logic',
#             'Is mapped manually to URLs',
#         ]
#         return Response({'spells': self.object.spell_name, 'an_apiview': an_apiview})

#     def post(self, request):
#         """create a hello message with our name"""
#         serializer = self.serializer(data=request.data)
#         if serializer.is_valid():
#             spell_name = serializer.validated_data.get('spell_name')
#             message = f'{spell_name}'
#             return Response({'spell': message})
#         else: 
#             return Response(
#                 serializer.errors, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )