# pylint: disable=missing-module-docstring
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       UsernameField)
from django.contrib.auth.models import User

from .models import Comment, Post, Suggestion

class SignupForm(UserCreationForm):
    """
    Form for user registration
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}))

    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={"class": "form-control"}))

    def clean_email(self):
        """
        this function checks the existing of mail
        """
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data["email"]
    class Meta:
        """
        Form for user registration
        """
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "pattern":"[0-9A-Za-z]+"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "pattern":"[A-Za-z]+"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "pattern":"[A-Za-z ]+"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }



class ProfileUpdate(forms.ModelForm):
    """
    form to update user profile information
    """
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)

    widgets = {
        "first_name": forms.TextInput(attrs={"class": "form-control"}),
        "last_name": forms.TextInput(attrs={"class": "form-control"}),
        "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
    class Meta:
        """
        Meta class for profile updation
        """
        model = User
        fields = ("email", "first_name", "last_name")

    def clean_email(self):
        """
        This method cleans the email
        """
        email = self.cleaned_data.get("email")
        return email


class LoginForm(AuthenticationForm):
    """
    Form for user login
    """
    username = UsernameField(widget=forms.TextInput(
        attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(
        attrs={"autofocus": True, "class": "form-control"}))


class PostForm(forms.ModelForm):
    """
    Form for making posts for blog
    """
    class Meta:
        """
        Form for making posts for blog
        """
        model = Post
        fields = ["title", "content", "author"]
        labels = {"title": "Title", "content": "Content", "author": "Author"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title of the post"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Blog Content goes here......"}),
            "author": forms.TextInput(
                attrs={"class": "form-control", "value": "", "id": "writer", "type": "hidden"}),
        }


class UpdateForm(UserCreationForm):
    """
    Form for updation of user data
    """
    class Meta:
        """
        Form for updation of user data
        """
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    """
    Form for making comments on posts
    """
    class Meta:
        """
        Form for making suggestions for blog
        """
        model = Comment
        fields = ["comment_content"]
        labels = {"comment_content": "Comment"}
        widgets = {
            "comment_content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "write Comment here"}),
        }


class SuggestionForm(forms.ModelForm):
    """
    Form for making suggestions for blog
    """
    class Meta:
        """
        Form for making suggestions for blog
        """
        model = Suggestion
        fields = ["suggestion_content"]
        labels = {"suggestion_content": "Suggestion"}
        widgets = {
            "suggestion_content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "your Suggestions here"}),
        }
