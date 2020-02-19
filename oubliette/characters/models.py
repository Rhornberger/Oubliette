from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Models for all character related information
class Craft(models.Model):
    craft = models.CharField(max_length=50, null=True, blank=True) 
       
    class Meta:
        ordering = ['craft']

    def __str__(self):
        return self.craft

class Knowledge(models.Model):
    knowledge = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['knowledge']

    def __str__(self):
        return self.knowledge

class Perform(models.Model):
    perform = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['perform']

    def __str__(self):
        return self.perform

class Profession(models.Model):
    profession = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['profession']

    def __str__(self):
        return self.profession

class Language(models.Model):
    language = models.CharField(max_length=50, null=True, blank=True)
    lan_speakers = models.CharField(max_length=500, null=True, blank=True)
    
    class Meta:
        ordering = ['language']

    def __str__(self):
        return self.language

class Weapon(models.Model):
    weapon = models.CharField(max_length=50, null=True, blank=True)
    weapon_category = models.CharField(max_length=50, null=True, blank=True)
    weapon_class = models.CharField(max_length=50, null=True, blank=True)
    weapon_price = models.CharField(max_length=50, null=True, blank=True)
    weapon_s_dmg = models.CharField(max_length=50, null=True, blank=True)
    weapon_m_dmg = models.CharField(max_length=50, null=True, blank=True)
    weapon_attack_bonus = models.IntegerField(null=True, blank=True)
    critical = models.CharField(max_length=50, null=True, blank=True)
    weapon_weight = models.CharField(max_length=50, null=True, blank=True)
    weapon_special = models.CharField(max_length=50, null=True, blank=True)
    weapon_type = models.CharField(max_length=50, null=True, blank=True)
    weapon_range = models.IntegerField(null=True, blank=True)
    ammunition = models.CharField(max_length=50, null=True, blank=True)
    
    
    
    class Meta:
        ordering = [
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
            ]

    def __str__(self):
        return self.weapon

class Ac_Item(models.Model):
    armour_class_item = models.CharField(max_length=50, null=True, blank=True)
    ac_cost = models.CharField(max_length=50, null=True, blank=True)
    ac_speed_b30 = models.CharField(max_length=50, null=True, blank=True)
    ac_speed_b20 = models.CharField(max_length=50, null=True, blank=True)
    ac_bonus = models.IntegerField(null=True, blank=True)
    ac_type = models.CharField(max_length=50, null=True, blank=True)
    ac_checkpenalty = models.IntegerField(null=True, blank=True)
    ac_spellfailure = models.IntegerField(null=True, blank=True)
    ac_weight = models.IntegerField(null=True, blank=True)
    ac_max_dex = models.CharField(max_length=50, null=True, blank=True)
    ac_properties = models.CharField(max_length=300, null=True, blank=True)
    
    class Meta:
        ordering = [
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
            ]

    def __str__(self):
        return self.armour_class_item

class Gear(models.Model):
    item = models.CharField(max_length=300, null=True, blank=True)
    item_wt = models.CharField(max_length=50, null=True, blank=True)
    item_cost = models.CharField(max_length=300, null=True, blank=True)
    item_type = models.CharField(max_length=300, null=True, blank=True)
    
    class Meta:
        ordering = ['item', 'item_wt', 'item_cost', 'item_type']

    def __str__(self):
        return self.item

class Feat(models.Model):
    feat = models.CharField(max_length=50, null=True, blank=True)
    feat_benefit = models.CharField(max_length=5000, null=True, blank=True)
    feat_type = models.CharField(max_length=500, null=True, blank=True)
    feat_prerequ = models.CharField(max_length=100, null=True, blank=True)
    feat_normal = models.CharField(max_length=5000, null=True, blank=True)
    feat_special = models.CharField(max_length=5000, null=True, blank=True)

    class Meta:
        ordering = [
            'feat', 
            'feat_benefit', 
            'feat_type', 
            'feat_prerequ', 
            'feat_normal', 
            'feat_special',
            ]

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
    Alignment = models.CharField(max_length=50, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    homeland = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
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
    weapon = models.ManyToManyField(Weapon, null=True, blank=True)
    language = models.ManyToManyField(Language, null=True, blank=True)
    acrobatics = models.IntegerField(null=True, blank=True)
    appraise = models.IntegerField(null=True, blank=True)
    bluff = models.IntegerField(null=True, blank=True)
    climb = models.IntegerField(null=True, blank=True)
    craft = models.ManyToManyField(Craft, null=True, blank=True)
    craft_mod = models.IntegerField(null=True, blank=True)
    diplomacy = models.IntegerField(null=True, blank=True)
    disable_device = models.IntegerField(null=True, blank=True)
    disguise = models.IntegerField(null=True, blank=True)
    escape_artist = models.IntegerField(null=True, blank=True)
    fly = models.IntegerField(null=True, blank=True)
    handle_animal = models.IntegerField(null=True, blank=True)
    heal = models.IntegerField(null=True, blank=True)
    intimidate = models.IntegerField(null=True, blank=True)
    knowledge = models.ManyToManyField(Knowledge, null=True, blank=True)
    knowledge_mod = models.IntegerField(null=True, blank=True)
    linguistics = models.IntegerField(null=True, blank=True)
    perception = models.IntegerField(null=True, blank=True)
    perform = models.ManyToManyField(Perform, null=True, blank=True)
    perform_mod = models.IntegerField(null=True, blank=True)
    profession = models.ManyToManyField(Profession, null=True, blank=True)
    profession_mod = models.IntegerField(null=True, blank=True)
    ride = models.IntegerField(null=True, blank=True)
    sense_motive = models.IntegerField(null=True, blank=True)
    sleight_of_hand = models.IntegerField(null=True, blank=True)
    spellcraft = models.IntegerField(null=True, blank=True)
    stealth = models.IntegerField(null=True, blank=True)
    survival = models.IntegerField(null=True, blank=True)
    swim = models.IntegerField(null=True, blank=True)
    use_magic_device = models.IntegerField(null=True, blank=True)
    ac_item = models.ManyToManyField(Ac_Item, null=True, blank=True)
    gear = models.ManyToManyField(Gear, null=True, blank=True)
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
    feat = models.ManyToManyField(Feat, null=True, blank=True)
    special_ability = models.ManyToManyField(Special_Ability, null=True, blank=True)
    spells_per_day = models.IntegerField(null=True, blank=True)
    spells_known = models.IntegerField(null=True, blank=True)
    domain_or_speciality_magic = models.CharField(max_length=300, null=True, blank=True)
    zero_lvl_spell = models.ManyToManyField(Zero_Lvl_Spell, null=True, blank=True)
    first_lvl_spell = models.ManyToManyField(First_Lvl_Spell, null=True, blank=True)
    second_lvl_spell = models.ManyToManyField(Second_Lvl_Spell, null=True, blank=True)
    third_lvl_spell = models.ManyToManyField(Third_Lvl_Spell, null=True, blank=True)
    fourth_lvl_spell = models.ManyToManyField(Fourth_Lvl_Spell,null=True, blank=True)
    fifth_lvl_spell = models.ManyToManyField(Fifth_Lvl_Spell,null=True, blank=True)
    sixth_lvl_spell = models.ManyToManyField(Sixth_Lvl_Spell,null=True, blank=True)
    seventh_lvl_spell = models.ManyToManyField(Seventh_Lvl_Spell, null=True, blank=True)
    eighth_lvl_spell = models.ManyToManyField(Eighth_Lvl_Spell, null=True, blank=True)
    ninth_lvl_spell = models.ManyToManyField(Ninth_Lvl_Spell,null=True, blank=True)
    xp = models.IntegerField(null=True, blank=True)
    xp_next_lvl = models.IntegerField(null=True, blank=True)
    note = models.ManyToManyField(Note, null=True, blank=True)

    img = models.ImageField(default='default.jpg', upload_to='character_pics') 

    def __str__(self):
        return f'{self.player_name} {self.character_name} {self.img} character' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.img.path) 


