from django.db import models

# Spell model for DB
class Spell(models.Model):
    """creating the tables for the spells model"""
    spell_name = models.CharField(max_length=50) #spell name
    school = models.CharField(max_length=50) #the school of magic the spell derives from 
    level = models.CharField(max_length=100) #the level the caster needs to be to cast the spell
    casting_time = models.CharField(max_length=50) #the amount of time it takes to cast the spell
    components = models.CharField(max_length=100) #the materials that might be needed to cast the spell
    spell_range = models.CharField(max_length=300) #the range of the spells effect
    target = models.CharField(max_length=300) #if the targets a specific person or is it an area effect
    duration = models.CharField(max_length=100) #the kind of effect the spell produces
    saving_throw = models.CharField(max_length=100) # can it be protected againts and by what means
    spell_resistance = models.CharField(max_length=100) #is there any innate deffense against this spell
    description = models.CharField(max_length=5000) #the general description of what the spell does
    
    def __str__(self):
        """this will return just the spells name when performing a search"""
        return f'{self.spell_name}'

# Race model for DB
class Race(models.Model):
    """creating the tables for character race quick reference model"""
    race_name = models.CharField(max_length=50) 
    general_description = models.CharField(max_length=5000) #general description of the race in question
    physical_description = models.CharField(max_length=5000) #physical descriptin of the race in question
    society = models.CharField(max_length=5000) #the way a race interacts with society as a whole
    relations = models.CharField(max_length=5000) #the way a race interacts with individuals and other races
    alignment_religion = models.CharField(max_length=5000) #the tendancies of the race toward religion and alignment
    adventurer = models.CharField(max_length=5000) #the race as they relate to adventures
    male_names = models.CharField(max_length=5000) #suggested male names
    female_names = models.CharField(max_length=5000) #suggested female names
    racial_traits = models.CharField(max_length=5000) # traits specific to the race
    size = models.CharField(max_length=1000) #size of race in question
    base_speed = models.CharField(max_length=1000) # the speed an unencumbered member of this race can move
    vision = models.CharField(max_length=1000) #the vision a race has lowlight/darkvision
    special_trait = models.CharField(max_length=5000) # special traits associated with the race
    weapon_familiarity = models.CharField(max_length=5000) # weapons that can be used by the race
    languages = models.CharField(max_length=5000) #languages that can be spoken to start with

    def __str__(self):
        """return race name when performing a search"""
        return f'{self.race_name}' 