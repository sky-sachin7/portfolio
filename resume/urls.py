
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/",views.about, name="about"),
    path("projects/", views.project, name="projects"),
    path("experience/", views.experience, name="experience"),
    path("education/", views.education, name="education"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume, name="resume")
]