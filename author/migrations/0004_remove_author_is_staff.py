# Generated by Django 5.0.6 on 2024-06-18 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0003_author_author_user_name_author_is_active_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="is_staff",
        ),
    ]
