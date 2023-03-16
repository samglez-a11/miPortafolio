from django.urls import path

from miPortafolioApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('trabajos', views.trabajos, name="trabajos"),
    path('about', views.about, name="about"),
    path('hobby', views.hobby, name="hobby")
]