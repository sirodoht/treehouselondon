# Generated by Django 5.0.2 on 2024-03-14 20:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_remove_place_dwelling_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="place",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]