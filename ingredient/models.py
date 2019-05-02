from django.db import models


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True, db_column='ingredient_id')
    name = models.CharField(max_length=50, unique=True)
    calories = models.IntegerField()


