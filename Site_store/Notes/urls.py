from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='store-home'),
	path('about/', views.about, name='about-site'),
	path('notes/', views.notes, name='notes'),
]