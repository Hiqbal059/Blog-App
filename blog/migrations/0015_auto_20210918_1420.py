# Generated by Django 3.2.6 on 2021-09-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    Auto Generated code
    """

    dependencies = [
        ("blog", "0014_auto_20210917_2305"),
    ]

    operations = [
        migrations.AddField(
            model_name="likes",
            name="comment",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
            related_name="comment_likes", to="blog.comment"),
        ),
        migrations.AddField(
            model_name="suggestion",
            name="reply",
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE,
            related_name="suggestion_reply", to="blog.suggestion"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE,
            related_name="reply", to="blog.comment"),
        ),
        migrations.AlterField(
            model_name="likes",
            name="post",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
            related_name="post_likes", to="blog.post"),
        ),
    ]
