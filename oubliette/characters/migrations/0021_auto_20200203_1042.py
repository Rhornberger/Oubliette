# Generated by Django 3.0.2 on 2020-02-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0020_auto_20200203_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gear',
            options={'ordering': ['item', 'item_wt', 'item_cost']},
        ),
        migrations.AddField(
            model_name='gear',
            name='item_cost',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]