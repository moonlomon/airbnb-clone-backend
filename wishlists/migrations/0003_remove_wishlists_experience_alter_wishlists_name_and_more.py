# Generated by Django 5.1.2 on 2025-01-30 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experience", "0002_initial"),
        ("rooms", "0002_initial"),
        (
            "wishlists",
            "0002_wishlists_experience_wishlists_name_wishlists_rooms_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wishlists",
            name="experience",
        ),
        migrations.AlterField(
            model_name="wishlists",
            name="name",
            field=models.CharField(max_length=150),
        ),
        migrations.RemoveField(
            model_name="wishlists",
            name="rooms",
        ),
        migrations.AlterField(
            model_name="wishlists",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="wishlists",
            name="experience",
            field=models.ManyToManyField(to="experience.experience"),
        ),
        migrations.AddField(
            model_name="wishlists",
            name="rooms",
            field=models.ManyToManyField(to="rooms.room"),
        ),
    ]
