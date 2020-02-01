from rest_framework import serializers
from django.contrib.auth.models import User

from references.models import Spell, Race
from users.models import Profile
from characters.models import Character
from characters.models import Craft
from characters.models import Knowledge
from characters.models import Perform
from characters.models import Profession
from characters.models import Language
from characters.models import Weapon
from characters.models import Ac_Item
from characters.models import Gear
from characters.models import Feat
from characters.models import Special_Ability
from characters.models import Zero_Lvl_Spell
from characters.models import First_Lvl_Spell
from characters.models import Second_Lvl_Spell
from characters.models import Third_Lvl_Spell
from characters.models import Fourth_Lvl_Spell
from characters.models import Fifth_Lvl_Spell
from characters.models import Sixth_Lvl_Spell
from characters.models import Seventh_Lvl_Spell
from characters.models import Eighth_Lvl_Spell
from characters.models import Ninth_Lvl_Spell
from characters.models import Note
# from parties.models import Party
# from characters.models import Character

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = (
            'id',
            'user',
            'img',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

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

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = (
            'id',
            'race_name',
            'general_description',
            'physical_description',
            'society',
            'relations',
            'alignment_religion',
            'adventurer',
            'male_names',
            'female_names',
            'racial_traits',
            'size',
            'base_speed',
            'vision',
            'special_trait',
            'weapon_familiarity',
            'languages'
        )

class CharacterSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(read_only=True, source="player_name")
    class Meta:
        model = Character
        fields = (
            'id',
            'player_name',
            'user_detail',
            'character_name', 
            'character_class',         
            'diety', 
            'race',
            'homeland',
            'size',
            'gender',
            'age',
            'height',
            'weight',
            'hair_color',
            'eye_color',
            'hit_points',
            'base_speed',
            'speed_with_armour',
            'fly_speed',
            'swim_speed',
            'climb_speed',
            'burrow_speed',
            'initiative',
            'strength',
            'strength_mod',
            'dexterity',
            'dexterity_mod',
            'constitution',
            'constitution_mod',
            'intelligence',
            'intelligence_mod',
            'wisdom',
            'wisdom_mod',
            'charisma',
            'charisma_mod',
            'armor_class',
            'touch_ac',
            'flat_footed_ac',
            'fortitude',
            'reflex',
            'will',
            'base_attack_bonus',
            'spell_resistance',
            'cmb',
            'cmd',
            'weapon',
            'language',
            'acrobatics',
            'appraise',
            'bluff',
            'climb',
            'craft',
            'diplomacy',
            'disable_device',
            'disguise',
            'escape_artist',
            'fly',
            'handle_animal',
            'heal',
            'intimidate',
            'knowledge',
            'linguistics',
            'perception',
            'perform',
            'profession',
            'ride',
            'sense_motive',
            'sleight_of_hand',
            'spellcraft',
            'stealth',
            'survival',
            'swim',
            'use_magic_device',
            'ac_item',
            'item',
            'light_load',
            'medium_load',
            'heavy_load',
            'lift_over_head',
            'lift_off_ground',
            'drag_or_push',
            'copper',
            'silver',
            'gold',
            'platinum',
            'feat',
            'special_ability',
            'spells_per_day',
            'spells_known',
            'domain_or_speciality_magic',
            'zero_lvl_spell',
            'first_lvl_spell',
            'second_lvl_spell',
            'third_lvl_spell',
            'fourth_lvl_spell',
            'fifth_lvl_spell',
            'sixth_lvl_spell',
            'seventh_lvl_spell',
            'eighth_lvl_spell',
            'ninth_lvl_spell',
            'note',
            'xp',
            'xp_next_lvl',
            'img',    
        )

class CraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craft
        fields = (
            'id',
            'craft',
            'craft_mod'
        )

class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = (
            'id',
            'knowledge',
            'knowledge_mod'
        )

class PerformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perform
        fields = (
            'id',
            'perform',
            'perform_mod'
        )

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = (
            'id',
            'profession',
            'profession_mod'
        )

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'language',
        )

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = (
            'id',
            'weapon', 
            'weapon_attack_bonus', 
            'critical', 
            'weapon_type', 
            'weapon_range', 
            'ammunition', 
            'damage'
        )

class Ac_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ac_Item
        fields = (
            'id',
            'armour_class_item', 
            'ac_bonus', 'ac_type', 
            'ac_checkpenalty', 
            'ac_spellfailure', 
            'ac_weight', 
            'ac_properties'
        )

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = (
            'id',
            'item',
            'item_wt'
        )

class FeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feat
        fields = (
            'id',
            'feat',
        )

class Special_AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Special_Ability
        fields = (
            'id',
            'special_ability',
        )

class Zero_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zero_Lvl_Spell
        fields = (
            'id',
            'zero_lvl_spell',
        )

class First_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = First_Lvl_Spell
        fields = (
            'id',
            'first_lvl_spell',
        )

class Second_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Second_Lvl_Spell
        fields = (
            'id',
            'second_lvl_spell',
        )

class Third_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Third_Lvl_Spell
        fields = (
            'id',
            'third_lvl_spell',
        )

class Fourth_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fourth_Lvl_Spell
        fields = (
            'id',
            'fourth_lvl_spell',
        )

class Fifth_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fifth_Lvl_Spell
        fields = (
            'id',
            'fifth_lvl_spell',
        )

class Sixth_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sixth_Lvl_Spell
        fields = (
            'id',
            'sixth_lvl_spell',
        )

class Seventh_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seventh_Lvl_Spell
        fields = (
            'id',
            'seventh_lvl_spell',
        )

class Eighth_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eighth_Lvl_Spell
        fields = (
            'id',
            'eighth_lvl_spell',
        )

class Ninth_Lvl_SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ninth_Lvl_Spell
        fields = (
            'id',
            'ninth_lvl_spell',
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'note'
        )