# Generated by Django 3.0.2 on 2020-01-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0003_auto_20200122_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='description',
            field=models.CharField(max_length=3000),
        ),
    ]