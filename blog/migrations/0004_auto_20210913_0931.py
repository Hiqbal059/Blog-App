# pylint: disable=missing-module-docstring
# Generated by Django 3.2.6 on 2021-09-13 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
"""
Auto generated code
"""

class Migration(migrations.Migration):
    """
    Auto generated code
    """
    dependencies = [
        ("blog", "0003_auto_20210910_1627"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suggestion",
            name="time",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2021, 9, 13, 9, 31, 14, 741298, tzinfo=utc)),
        ),
    ]
