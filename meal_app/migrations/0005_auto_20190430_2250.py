# Generated by Django 2.0.10 on 2019-04-30 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0004_meal_date_filed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='date_filed',
            new_name='date_fieled',
        ),
    ]
