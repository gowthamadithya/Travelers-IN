# Generated by Django 5.1.1 on 2024-10-18 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="name",
            new_name="category_name",
        ),
    ]