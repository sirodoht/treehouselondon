# Generated by Django 5.0.2 on 2024-03-16 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_remove_place_member_count_alter_place_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
