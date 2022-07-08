# pylint: disable=invalid-name, missing-module-docstring, unused-import
from django.conf.urls import handler400, handler404
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls"))
]
handler404 = 'blog.views.error_404_handler.error_404_view'
handler400 = 'blog.views.error_404_handler.error_404_view'
