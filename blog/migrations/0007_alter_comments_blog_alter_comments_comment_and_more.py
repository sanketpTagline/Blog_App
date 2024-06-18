# Generated by Django 5.0.6 on 2024-06-18 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_comments_blog_comments_date_added_comments_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.blog",
            ),
        ),
        migrations.AlterField(
            model_name="comments",
            name="comment",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="comments",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
