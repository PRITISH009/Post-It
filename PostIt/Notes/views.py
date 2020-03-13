from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('<h1>Notes Wall</h1>')

def  about(req):
    return HttpResponse('<h1>About Page</h1><p>This is a Web App you can use to stick all your notes or tasks to be completed on your own personal wall</p>')