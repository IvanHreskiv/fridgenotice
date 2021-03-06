# Generated by Django 2.0.10 on 2019-05-03 11:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredient', '0001_initial'),
        ('meal_app', '0007_auto_20190501_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('recipe', models.CharField(max_length=500)),
                ('date_field', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=200)),
                ('ingredient', models.ForeignKey(db_column='ingredient_id', on_delete=django.db.models.deletion.CASCADE, to='ingredient.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe.RecipeIngredient', to='ingredient.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_app.Meal'),
        ),
    ]
