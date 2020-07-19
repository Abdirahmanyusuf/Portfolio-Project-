from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('Cv/', views.Cv, name="Cv"),
    path('project/', views.project, name="project"),

]
