# pylint: disable=missing-module-docstring
# Generated by Django 3.2.6 on 2021-09-15 12:32
"""
Auto generated code
"""
from django.db import migrations, models

import ckeditor.fields

class Migration(migrations.Migration):
    """
    Auto generated code
    """
    dependencies = [
        ("blog", "0010_auto_20210914_1646"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="suggestion",
            name="time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
