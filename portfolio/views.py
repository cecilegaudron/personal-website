# Import to deploy view
from django.shortcuts import render


def index(request):
    """
    Basic view for Home Page
    """
    return render(request, 'index.html', {})


def contact(request):
    """
    Basic view for Contact section
    """
    return render(request, 'contact.html', {})


def about(request):
    """
    Basic view for About section
    """
    return render(request, 'about.html', {})


def services(request):
    """
    Basic view for Services Page
    """
    return render(request, 'services.html', {})

def projects(request):
    """
    Basic view for Projects Page
    """
    return render(request, 'projects.html', {})