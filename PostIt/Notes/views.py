from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from .models import Notes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class NoteListView(LoginRequiredMixin,ListView):
    additional_context = {}
    model = Notes
    context_object_name = 'posts'
    template_name = 'Notes/wall.html'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        queryset = Notes.objects.filter(user = self.request.user.id)
        return queryset


class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin ,DetailView):
    model = Notes

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False


class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    fields = ['task', 'description']
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    fields = ['task', 'description']
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes
    success_url = '/'
    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False


def  about(req):
    return render(req, 'Notes/about.html', {'title' : 'About Page'})

