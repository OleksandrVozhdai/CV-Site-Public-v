from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path("", views.IndexView, name="Home"),
    path("csProj/", views.csProjectsView, name="csProjects"),
    path("pthProj/", views.pthProjectsView, name="pthProjects"),
    path("about/", views.aboutView, name="about"),
    path("skills/", views.skillsView, name="skills"),
    path("contact/", views.contactView, name="contact"),
    path("resume/", views.resumeView, name="resume"),
]