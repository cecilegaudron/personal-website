from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name="index"),
    path('index.html/', views.contact, name="contact"),
    path('services.html', views.services, name="services"),
    path('about.html', views.about, name="about"),
    path('projects.html', views.projects, name="projects"),
    path('contact.html', views.contact, name="contact"),
]
