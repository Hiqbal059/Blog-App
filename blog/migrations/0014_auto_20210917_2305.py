# Generated by Django 3.2.6 on 2021-09-17 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    Auto Generated code
    """
    dependencies = [
        ("blog", "0013_auto_20210915_1423"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_reported",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name="reply", null=True, to="blog.comment"),
        ),
        migrations.AddField(
            model_name="post",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="post",
            name="is_reported",
            field=models.BooleanField(default=False),
        ),
    ]
