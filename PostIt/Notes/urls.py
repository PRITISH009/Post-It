from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='notes-wall'),
    path('about', views.about, name = 'about-post-it'),
]