# Generated by Django 3.0.2 on 2020-02-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0024_auto_20200203_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='Alignment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
