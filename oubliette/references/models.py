from django.db import models

# Create your models here.
class Spell(models.Model):
    """creating the tables for the spells model"""
    spell_name = models.CharField(max_length=50) #spell name
    school = models.CharField(max_length=50) #the school of magic the spell derives from 
    level = models.CharField(max_length=100) #the level the caster needs to be to cast the spell
    casting_time = models.CharField(max_length=50) #the amount of time it takes to cast the spell
    components = models.CharField(max_length=100) #the materials that might be needed to cast the spell
    spell_range = models.CharField(max_length=100) #the range of the spells effect
    target = models.CharField(max_length=100) #if the targets a specific person or is it an area effect
    duration = models.CharField(max_length=100) #the kind of effect the spell produces
    saving_throw = models.CharField(max_length=100) # can it be protected againts and by what means
    spell_resistance = models.CharField(max_length=100) #is there any innate deffense against this spell
    description = models.CharField(max_length=3000) #the general description of what the spell does
    
    def __str__(self):
        """this will return just the spells name when performing a search"""
        return f'{self.spell_name}'