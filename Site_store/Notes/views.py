from django.shortcuts import render
from .models import Notes
from .forms import NewNoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html', {'title': 'О магазине PROASS'})


@login_required
def notes(request):
    context = {
        'notes': Notes.objects.filter(user=request.user)
    }
    return render(request, 'my_notes.html', context)


# class NoteListView(ListView):
#     model = Notes
#     template_name = 'my_notes.html'
#     context_object_name = 'Notes'
#     ordering = ['-date_posted']
#
#
class NoteDetailView(DetailView):
    model = Notes
    template_name = 'note_detail.html'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    template_name = 'note_form.html'
    fields = ['title', 'content']

    def get_form_class(self):
        return NewNoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    fields = ['title', 'content']

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
    success_url = '/notes/'
    template_name = 'note_confirm_delete.html'

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     messages.success(self.request, 'Note successfully deleted!')
    #     return HttpResponseRedirect(success_url)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False