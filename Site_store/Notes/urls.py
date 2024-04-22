from django.urls import path
from . import views
from .views import NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView

urlpatterns = [
	path('', views.home, name='store-home'),
	path('about/', views.about, name='about-site'),
	path('notes/', views.notes, name='notes'),
	path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
	path('notes/new/', NoteCreateView.as_view(), name='note-create'),
	path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
	path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
