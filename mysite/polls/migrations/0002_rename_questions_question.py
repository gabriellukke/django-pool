# Generated by Django 4.1.1 on 2022-09-22 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Questions",
            new_name="Question",
        ),
    ]
