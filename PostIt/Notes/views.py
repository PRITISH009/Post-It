from django.shortcuts import render
from .models import Notes

context = {
    'title' : 'My Wall',
    'posts' : Notes.objects.all()
}


# Create your views here.
def home(req):
    if req.user.is_authenticated:
        return render(req, 'Notes/wall.html', context)
    else:
        return render(req, 'Notes/web_app_home.html')

def  about(req):
    return render(req, 'Notes/about.html', {'title' : 'About Page'})

