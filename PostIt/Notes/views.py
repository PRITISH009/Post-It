from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Notes


@method_decorator(login_required, name='dispatch')
class NoteListView(ListView):
    additional_context = {}
    model = Notes
    context_object_name = 'posts'
    template_name = 'Notes/wall.html'
    ordering = ['-date_posted']

    def get_queryset(self):
        queryset = Notes.objects.filter(user = self.request.user.id)
        return queryset

def home(req):
    context = {
        'title' : 'My Wall',
        'posts' : Notes.objects.filter(user=req.user.id)
    }

    if req.user.is_authenticated:
        return render(req, 'Notes/wall.html', context)
    else:
        return render(req, 'Notes/web_app_home.html')


def  about(req):
    return render(req, 'Notes/about.html', {'title' : 'About Page'})

