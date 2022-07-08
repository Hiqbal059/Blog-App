# pylint: disable=too-many-ancestors, arguments-differ
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import LoginForm


class LoginUser(LoginView):
    """
    This class will Login the user
    """
    def post(self, request):
        """
        this function will login the user
        """
        login(self.request)
        return HttpResponse(self.request, '{} you have logged in successfully'.format(request.user))

    def get(self, request):
        """
        this function will return login form
        """
        form = LoginForm()
        context = {"form":form}
        return render(request, "registration/login.html", context)
