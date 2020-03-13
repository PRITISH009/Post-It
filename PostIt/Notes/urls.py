from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Notes Wall'),
    path('about', views.about, name = 'About Post-It'),
]