from rest_framework import serializers
from django.contrib.auth.models import User

from references.models import Spell
from users.models import Profile
# from parties.models import Party
# from characters.models import Character

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        feilds = (
            'user',
            'img',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class SpellSerializer(serializers.ModelSerializer):
    """Serializer fields for testing our APIViews"""
    class Meta:
        model = Spell
        fields = (
            'id',
            'spell_name',
            'school',
            'level',
            'casting_time',
            'components',
            'spell_range',
            'target',
            'duration',
            'saving_throw',
            'spell_resistance',
            'description'
        )


        

# class CharacterSerializer(serializers.ModelSerializer):
#     # author_detail = CharacterSerializer(read_only=True, source="author")
#     class Meta:
#         model = Character
#         fields = ('class', 'race', 'gender', 'age')