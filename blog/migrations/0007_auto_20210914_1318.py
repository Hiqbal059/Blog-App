# pylint: disable=missing-module-docstring
# Generated by Django 3.2.6 on 2021-09-14 13:18
"""
Auto generated code
"""
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    """
    Auto generated code
    """
    dependencies = [
        ("blog", "0006_auto_20210913_1250"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suggestion",
            name="time",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2021, 9, 14, 13, 18, 29, 923286, tzinfo=utc)),
        ),
    ]
