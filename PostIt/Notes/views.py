from django.shortcuts import render
from .models import Notes

context = {
    'title' : 'My Wall',
    'posts' : Notes.objects.all()
}


# Create your views here.
def home(req):
    return render(req, 'Notes/wall.html', context)

def  about(req):
    return render(req, 'Notes/about.html', {'title' : 'About Page'})