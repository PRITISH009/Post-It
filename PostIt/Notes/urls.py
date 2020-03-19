from django.urls import path
from .views import NoteListView
from . import views

urlpatterns = [
    path('', NoteListView.as_view() , name='notes-wall'),
    path('about', views.about, name = 'about-post-it'),
]