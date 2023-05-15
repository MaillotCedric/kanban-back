from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_, name="login"),
    path("logout", views.logout_, name="logout"),
    path("home", views.home, name="home"),
]
