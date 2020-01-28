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
from references.models import Spell
from users.models import Profile
from .serializers import SpellSerializer #this will Serialize the info from the bd on spells
from .serializers import UserSerializer  #this will Serialize the info from the bd on users
from .serializers import ProfileSerializer #this will serialize the info from DB on profiles
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# class CharacterViewSet(viewsets.ModelViewSet):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer

class ProfileViewSet(viewsets.ModelViewSet):
   queryset = Profile.objects.all()
   serializer_class = ProfileSerializer
    
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