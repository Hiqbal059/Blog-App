# pylint: disable=missing-module-docstring, invalid-name
from django.contrib.auth import urls as URLS
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from django_email_verification import urls as email_urls

from blog.views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("viewpost/<int:pk>", ViewPost.as_view(), name="viewpost"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("signup", UserRegister.as_view(), name="signup"),
    path("login", include(URLS), name="login"),
    path("logout", include(URLS), name="logout"),
    path("addpost", CreatePost.as_view(), name="addpost"),
    path("editpost/<int:pk>", UpdatePost.as_view(), name="editpost"),
    path("delpost/<int:pk>/remove", DeletePost.as_view(), name="delpost"),
    path("updateprofile/", UpdateProfile.as_view(), name="updateprofile"),
    path("like", LikePost.as_view(), name="like_post"),
    path("viewpost/comment", AddComment.as_view(), name="comment"),
    path("viewpost/", AddSuggestion.as_view(), name="suggestion"),
    path("suggestion/<int:pk>", SuggestionPanel.as_view(), name="suggestionpanel"),
    path("report/", Report.as_view(), name="report"),
    path("likecomment", LikeComment.as_view(), name="like_comment"),
    path("viewpost/<int:pk>/comment/<int:id>", AddComment.as_view, name="reply"),
    path("email/", include(email_urls)),
    path("suggestion/suggestion_action/", SuggestionAction.as_view(), name="suggestion_action"),
    path("dashboard/action", ModeratorActions.as_view(), name="moderator_action"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
