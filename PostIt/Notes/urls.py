from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView
from . import views

urlpatterns = [
    path('', NoteListView.as_view() , name='notes-wall'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='notes-update'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='notes-delete'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('about', views.about, name = 'about-post-it'),
]