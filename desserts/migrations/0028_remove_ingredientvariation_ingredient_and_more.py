# Generated by Django 5.0.3 on 2024-04-18 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("desserts", "0027_rename_dessert_photo_dessertvariation_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredientvariation",
            name="ingredient",
        ),
        migrations.AddField(
            model_name="dessertvariation",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="variation_desserts", to="desserts.ingredient"
            ),
        ),
        migrations.AddField(
            model_name="ingredientvariation",
            name="dessert_variation",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ingredient_variations",
                to="desserts.dessertvariation",
            ),
        ),
    ]
