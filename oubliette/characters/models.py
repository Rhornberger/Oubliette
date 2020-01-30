from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Craft(models.Model):
    craft = models.CharField(max_length=50, null=True, blank=True)
    craft_mod = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['craft', 'craft_mod']

    def __str__(self):
        return self.craft

class Knowledge(models.Model):
    knowledge = models.CharField(max_length=50, null=True, blank=True)
    knowledge_mod = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['knowledge', 'knowledge_mod']

    def __str__(self):
        return self.knowledge

class Perform(models.Model):
    perform = models.CharField(max_length=50, null=True, blank=True)
    perform_mod = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['perform', 'perform_mod']

    def __str__(self):
        return self.perform

class Profession(models.Model):
    profession = models.CharField(max_length=50, null=True, blank=True)
    profession_mod = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['profession', 'profession_mod']

    def __str__(self):
        return self.profession

class Language(models.Model):
    language = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['language']

    def __str__(self):
        return self.language

class Weapon(models.Model):
    weapon = models.CharField(max_length=50, null=True, blank=True)
    weapon_attack_bonus = models.IntegerField(null=True, blank=True)
    critical = models.IntegerField(null=True, blank=True)
    weapon_type = models.CharField(max_length=50, null=True, blank=True)
    weapon_range = models.IntegerField(null=True, blank=True)
    ammunition = models.CharField(max_length=50, null=True, blank=True)
    damage = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = [
            'weapon', 
            'weapon_attack_bonus', 
            'critical', 
            'weapon_type', 
            'weapon_range', 
            'ammunition', 
            'damage'
            ]

    def __str__(self):
        return self.weapon

class Ac_Item(models.Model):
    armour_class_item = models.CharField(max_length=50, null=True, blank=True)
    ac_bonus = models.IntegerField(null=True, blank=True)
    ac_type = models.CharField(max_length=50, null=True, blank=True)
    ac_checkpenalty = models.IntegerField(null=True, blank=True)
    ac_spellfailure = models.IntegerField(null=True, blank=True)
    ac_weight = models.IntegerField(null=True, blank=True)
    ac_properties = models.CharField(max_length=300, null=True, blank=True)
    
    class Meta:
        ordering = [
            'armour_class_item', 
            'ac_bonus', 'ac_type', 
            'ac_checkpenalty', 
            'ac_spellfailure', 
            'ac_weight', 
            'ac_properties'
            ]

    def __str__(self):
        return self.armour_class_item

class Gear(models.Model):
    item = models.CharField(max_length=300, null=True, blank=True)
    item_wt = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['item', 'item_wt']

    def __str__(self):
        return self.item

class Feat(models.Model):
    feat = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['feat']

    def __str__(self):
        return self.feat

class Special_Ability(models.Model):
    special_ability = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['special_ability']

    def __str__(self):
        return self.special_ability

class Zero_Lvl_Spell(models.Model):
    zero_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['zero_lvl_spell']

    def __str__(self):
        return self.zero_lvl_spell

class First_Lvl_Spell(models.Model):
    first_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['first_lvl_spell']

    def __str__(self):
        return self.first_lvl_spell

class Second_Lvl_Spell(models.Model):
    second_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['second_lvl_spell']

    def __str__(self):
        return self.second_lvl_spell

class Third_Lvl_Spell(models.Model):
    third_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['third_lvl_spell']

    def __str__(self):
        return self.third_lvl_spell

class Fourth_Lvl_Spell(models.Model):
    fourth_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['fourth_lvl_spell']

    def __str__(self):
        return self.fourth_lvl_spell

class Fifth_Lvl_Spell(models.Model):
    fifth_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['fifth_lvl_spell']

    def __str__(self):
        return self.fifth_lvl_spell

class Sixth_Lvl_Spell(models.Model):
    sixth_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['sixth_lvl_spell']

    def __str__(self):
        return self.sixth_lvl_spell

class Seventh_Lvl_Spell(models.Model):
    seventh_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['seventh_lvl_spell']

    def __str__(self):
        return self.seventh_lvl_spell

class Eighth_Lvl_Spell(models.Model):
    eighth_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['eighth_lvl_spell']

    def __str__(self):
        return self.eighth_lvl_spell

class Ninth_Lvl_Spell(models.Model):
    ninth_lvl_spell = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['ninth_lvl_spell']

    def __str__(self):
        return self.ninth_lvl_spell

class Note(models.Model):
    note = models.CharField(max_length=5000, null=True, blank=True)

    class Meta:
        ordering = ['note']

    def __str__(self):
        return self.note
    

class Character(models.Model):
    player_name = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=50, null=True, blank=True)
    character_class = models.CharField(max_length=50, null=True, blank=True)
    diety = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    homeland = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    hair_color = models.CharField(max_length=50, null=True, blank=True)
    eye_color = models.CharField(max_length=50, null=True, blank=True)
    hit_points = models.IntegerField(null=True, blank=True)
    base_speed = models.CharField(max_length=50, null=True, blank=True)
    speed_with_armour = models.IntegerField(null=True, blank=True)
    fly_speed = models.IntegerField(null=True, blank=True)
    swim_speed = models.IntegerField(null=True, blank=True)
    climb_speed = models.IntegerField(null=True, blank=True)
    burrow_speed = models.IntegerField(null=True, blank=True)
    initiative = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    strength_mod = models.IntegerField(null=True, blank=True)
    dexterity = models.IntegerField(null=True, blank=True)
    dexterity_mod = models.IntegerField(null=True, blank=True)
    constitution = models.IntegerField(null=True, blank=True)
    constitution_mod = models.IntegerField(null=True, blank=True)
    intelligence = models.IntegerField(null=True, blank=True)
    intelligence_mod = models.IntegerField(null=True, blank=True)
    wisdom = models.IntegerField(null=True, blank=True)
    wisdom_mod = models.IntegerField(null=True, blank=True)
    charisma = models.IntegerField(null=True, blank=True)
    charisma_mod = models.IntegerField(null=True, blank=True)
    armor_class = models.IntegerField(null=True, blank=True)
    touch_ac = models.IntegerField(null=True, blank=True)
    flat_footed_ac = models.IntegerField(null=True, blank=True)
    fortitude = models.IntegerField(null=True, blank=True)
    reflex = models.IntegerField(null=True, blank=True)
    will = models.IntegerField(null=True, blank=True)
    base_attack_bonus = models.IntegerField(null=True, blank=True)
    spell_resistance = models.IntegerField(null=True, blank=True)
    cmb = models.IntegerField(null=True, blank=True)
    cmd = models.IntegerField(null=True, blank=True)
    weapon = models.ManyToManyField(Weapon)
    language = models.ManyToManyField(Language)
    acrobatics = models.IntegerField(null=True, blank=True)
    appraise = models.IntegerField(null=True, blank=True)
    bluff = models.IntegerField(null=True, blank=True)
    climb = models.IntegerField(null=True, blank=True)
    craft = models.ManyToManyField(Craft)
    diplomacy = models.IntegerField(null=True, blank=True)
    disable_device = models.IntegerField(null=True, blank=True)
    disguise = models.IntegerField(null=True, blank=True)
    escape_artist = models.IntegerField(null=True, blank=True)
    fly = models.IntegerField(null=True, blank=True)
    handle_animal = models.IntegerField(null=True, blank=True)
    heal = models.IntegerField(null=True, blank=True)
    intimidate = models.IntegerField(null=True, blank=True)
    knowledge = models.ManyToManyField(Knowledge)
    linguistics = models.IntegerField(null=True, blank=True)
    perception = models.IntegerField(null=True, blank=True)
    perform = models.ManyToManyField(Perform)
    profession = models.ManyToManyField(Profession)
    ride = models.IntegerField(null=True, blank=True)
    sense_motive = models.IntegerField(null=True, blank=True)
    sleight_of_hand = models.IntegerField(null=True, blank=True)
    spellcraft = models.IntegerField(null=True, blank=True)
    stealth = models.IntegerField(null=True, blank=True)
    survival = models.IntegerField(null=True, blank=True)
    swim = models.IntegerField(null=True, blank=True)
    use_magic_device = models.IntegerField(null=True, blank=True)
    ac_item = models.ManyToManyField(Ac_Item)
    item = models.ManyToManyField(Gear)
    light_load = models.IntegerField(null=True, blank=True)
    medium_load = models.IntegerField(null=True, blank=True)
    heavy_load = models.IntegerField(null=True, blank=True)
    lift_over_head = models.IntegerField(null=True, blank=True)
    lift_off_ground = models.IntegerField(null=True, blank=True)
    drag_or_push = models.IntegerField(null=True, blank=True)
    copper = models.IntegerField(null=True, blank=True)
    silver = models.IntegerField(null=True, blank=True)
    gold = models.IntegerField(null=True, blank=True)
    platinum = models.IntegerField(null=True, blank=True)
    feat = models.ManyToManyField(Feat)
    special_ability = models.ManyToManyField(Special_Ability)
    spells_per_day = models.IntegerField(null=True, blank=True)
    spells_known = models.IntegerField(null=True, blank=True)
    domain_or_speciality_magic = models.CharField(max_length=300, null=True, blank=True)
    zero_lvl_spell = models.ManyToManyField(Zero_Lvl_Spell)
    first_lvl_spell = models.ManyToManyField(First_Lvl_Spell)
    second_lvl_spell = models.ManyToManyField(Second_Lvl_Spell)
    third_lvl_spell = models.ManyToManyField(Third_Lvl_Spell)
    fourth_lvl_spell = models.ManyToManyField(Fourth_Lvl_Spell)
    fifth_lvl_spell = models.ManyToManyField(Fifth_Lvl_Spell)
    sixth_lvl_spell = models.ManyToManyField(Sixth_Lvl_Spell)
    seventh_lvl_spell = models.ManyToManyField(Seventh_Lvl_Spell)
    eighth_lvl_spell = models.ManyToManyField(Eighth_Lvl_Spell)
    ninth_lvl_spell = models.ManyToManyField(Ninth_Lvl_Spell)
    xp = models.IntegerField(null=True, blank=True)
    xp_next_lvl = models.IntegerField(null=True, blank=True)
    note = models.ManyToManyField(Note)

    img = models.ImageField(default='default.jpg', upload_to='character_pics') 

    def __str__(self):
        return f'{self.character.player_name} {self.character.character_name} {self.character.img} character' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.img.path) 


