# Generated by Django 5.0.3 on 2024-04-15 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chef",
            old_name="first_name",
            new_name="full_name",
        ),
        migrations.RemoveField(
            model_name="chef",
            name="last_name",
        ),
    ]
