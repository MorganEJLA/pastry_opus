# Generated by Django 5.0.3 on 2024-04-16 21:31

import desserts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("desserts", "0012_alter_dessert_locale_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dessert",
            name="category_add",
            field=desserts.models.MultiSelectField(
                choices=[
                    ("Cakes", "Cakes"),
                    ("Pies & Tarts", "Pies & Tarts"),
                    ("Cookies & Bars", "Cookies & Bars"),
                    ("Pastries", "Pastries"),
                    ("Puddings & Custards", "Puddings & Custards"),
                    ("Frozen Desserts", "Frozen Desserts"),
                    ("Confections & Candies", "Confections & Candies"),
                    ("Fruit Desserts", "Fruit Desserts"),
                    ("Fried Dough", "Fried Dough"),
                ],
                null=True,
            ),
        ),
    ]
