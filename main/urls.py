from django.urls import path
from  . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("home/", views.home,name="home"),
    path("contact/", views.contact,name="contact"),
    path("projects/<int:id>/", views.project,name="project"),
    path("about_me/", views.about_me, name="about_me"),
]
