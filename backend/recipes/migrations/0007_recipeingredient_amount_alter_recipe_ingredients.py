# Generated by Django 4.1.5 on 2023-02-14 05:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Мин. количество ингридиентов 1')], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='recipes.ingredient'),
        ),
    ]
