from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'Notes/wall.html')

def  about(req):
    return render(req, 'Notes/about.html')