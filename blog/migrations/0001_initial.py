# pylint: disable=missing-module-docstring
# Generated by Django 3.2.6 on 2021-09-09 13:53
"""
Auto generated code
"""
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    """
    Auto generated code
    """
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("time", models.DateTimeField(
                    verbose_name=datetime.datetime(2021, 9, 9, 13, 53, 47, 196564, tzinfo=utc))),
                ("author", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                ("id", models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("suggestion_content", models.TextField()),
                ("time", models.DateTimeField(
                    verbose_name=datetime.datetime(2021, 9, 9, 13, 53, 47, 197329, tzinfo=utc))),
                ("suggestion_user", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ("suggetion_post", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to="blog.post")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("comment_content", models.TextField()),
                ("time", models.DateTimeField(
                    verbose_name=datetime.datetime(2021, 9, 9, 13, 53, 47, 196951, tzinfo=utc))),
                ("comment_post", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to="blog.post")),
                ("comment_user", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]