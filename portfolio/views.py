# Import to deploy view
from django.shortcuts import render


def index(request):
    """
    Basic view for Home Page
    """
    return render(request, 'index.html', {})