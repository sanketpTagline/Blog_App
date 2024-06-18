# Generated by Django 5.0.6 on 2024-06-13 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_name", models.CharField(max_length=120)),
                (
                    "author_age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(200),
                        ]
                    ),
                ),
                ("author_email", models.EmailField(max_length=254)),
                (
                    "author_profile_picture",
                    models.ImageField(
                        default="avatar.jpg", upload_to="profile_avatars"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
