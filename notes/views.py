from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    paginate_by = 10

class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_details.html'
    context_object_name = 'note'
