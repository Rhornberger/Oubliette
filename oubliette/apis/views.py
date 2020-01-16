from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt # for csrf_exempt
from django.utils.decorators import mathod_decorator # for csrf_exempt

from character.models import Character
from .serializers import CharacterSerializer, UserSerializer

# Create your views here.

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
