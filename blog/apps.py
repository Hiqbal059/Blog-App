# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Blogapp configuration
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
