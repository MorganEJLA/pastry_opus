# Generated by Django 5.0.3 on 2024-04-16 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "desserts",
            "0018_remove_dessert_category_remove_dessert_category_add_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="dessert",
            old_name="categories",
            new_name="category",
        ),
    ]
