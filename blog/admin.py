# pylint: disable=missing-module-docstring
from django.contrib import admin

from .models import Comment, Post, Suggestion, Likes

# Register your models here.

admin.site.register([Post, Suggestion, Comment, Likes])
