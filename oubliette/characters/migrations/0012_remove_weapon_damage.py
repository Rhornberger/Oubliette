# Generated by Django 3.0.2 on 2020-02-03 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_weapon_damage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='damage',
        ),
    ]
