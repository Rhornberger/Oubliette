from rest_framework import serializers
from django.contrib.auth.models import User

from characters.models import Character
# from parties.models import Party
# from references.models import Refernce

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class CharacterSerializer(serializers.ModelSerializer):
    # author_detail = CharacterSerializer(read_only=True, source="author")
    class Meta:
        model = Character
        fields = ('class', 'race', 'gender', 'age')