# Generated by Django 2.0.10 on 2019-04-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('detail', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
