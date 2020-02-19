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

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = (
            'id',
            'weapon', 
            'weapon_category',
            'weapon_class',
            'weapon_price',
            'weapon_s_dmg',
            'weapon_m_dmg',
            'weapon_weight',
            'weapon_special',
            'weapon_attack_bonus', 
            'critical', 
            'weapon_type', 
            'weapon_range', 
            'ammunition', 
        )



class CraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craft
        fields = (
            'id',
            'craft',
        )

class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = (
            'id',
            'knowledge',
        )

class PerformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perform
        fields = (
            'id',
            'perform',
        )

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = (
            'id',
            'profession',
        )

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'language',
            'lan_speakers',
        )



class Ac_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ac_Item
        fields = (
            'id',
            'armour_class_item',
            'ac_cost',
            'ac_speed_b30',
            'ac_speed_b20', 
            'ac_bonus', 
            'ac_type', 
            'ac_checkpenalty', 
            'ac_spellfailure', 
            'ac_weight',
            'ac_max_dex', 
            'ac_properties'
        )

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = (
            'id',
            'item',
            'item_wt',
            'item_cost',
            'item_type'
        )

class FeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feat
        fields = (
            'id',
            'feat', 
            'feat_benefit', 
            'feat_type', 
            'feat_prerequ', 
            'feat_normal', 
            'feat_special',
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

class CharacterSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(read_only=True, source="player_name")
    weapon_info = WeaponSerializer(read_only=True, many=True, source="weapon")
    language_info = LanguageSerializer(read_only=True, many=True, source="language")
    craft_info = CraftSerializer(read_only=True, many=True, source="craft")
    knowledge_info = KnowledgeSerializer(read_only=True, many=True, source="knowledge")
    ac_item_info = Ac_ItemSerializer(read_only=True, many=True, source="ac_item")
    gear_info = GearSerializer(read_only=True, many=True, source="gear")
    feat_info = FeatSerializer(read_only=True, many=True, source="feat")
    special_ability_info = Special_AbilitySerializer(read_only=True, many=True, source="special_ability")
    note_info = NoteSerializer(read_only=True, many=True, source="note")
    perform_info = PerformSerializer(read_only=True, many=True, source="perform")
    class Meta:
        model = Character
        fields = (
            'id',
            'player_name',
            'user_detail',
            'character_name', 
            'character_class',         
            'diety', 
            'Alignment',
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
            'weapon_info',
            'language',
            'language_info',
            'acrobatics',
            'appraise',
            'bluff',
            'climb',
            'craft',
            'craft_info',
            'craft_mod',
            'diplomacy',
            'disable_device',
            'disguise',
            'escape_artist',
            'fly',
            'handle_animal',
            'heal',
            'intimidate',
            'knowledge',
            'knowledge_info',
            'knowledge_mod',
            'linguistics',
            'perception',
            'perform',
            'perform_info',
            'perform_mod',
            'profession',
            'profession_mod',
            'ride',
            'sense_motive',
            'sleight_of_hand',
            'spellcraft',
            'stealth',
            'survival',
            'swim',
            'use_magic_device',
            'ac_item',
            'ac_item_info',
            'gear',
            'gear_info',
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
            'feat_info',
            'special_ability',
            'special_ability_info',
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
            'note_info',
            'xp',
            'xp_next_lvl',
            'img',    
        )