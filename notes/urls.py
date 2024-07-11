from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='list_notes'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='detail_notes'),
]