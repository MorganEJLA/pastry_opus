# Generated by Django 5.0.3 on 2024-04-18 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("desserts", "0026_dessertvariation_dessert_photo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dessertvariation",
            old_name="dessert_photo",
            new_name="image",
        ),
        migrations.RenameField(
            model_name="dessertvariation",
            old_name="dessert_photo_2",
            new_name="image_2",
        ),
    ]
