# Generated by Django 5.0.3 on 2024-04-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("desserts", "0005_alter_dessert_featured_ingredient_photo_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dessert",
            name="description",
            field=models.TextField(max_length=800),
        ),
    ]
