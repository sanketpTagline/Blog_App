# Generated by Django 5.0.6 on 2024-06-19 05:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_comments_blog_alter_comments_comment_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="name",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
