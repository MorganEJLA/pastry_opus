# Generated by Django 5.0.3 on 2024-04-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_rename_first_name_chef_full_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chef",
            name="locale",
            field=models.CharField(default="none", max_length=100),
        ),
    ]
