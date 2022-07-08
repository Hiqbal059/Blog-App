# pylint: disable=unused-argument

from django.shortcuts import render

def error_404_view(request, exception):
    """
    This function handles the exception error 404
    """
    data = {"name": request.user}
    return render(request, 'error_404.html', data)
