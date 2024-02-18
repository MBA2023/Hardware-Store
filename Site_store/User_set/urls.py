from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="main_page"),
    # path("reg/", views.registration, name="new_user"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("notes/", views.notes, name="notes"),
    # path("add_note/", views.add_note, name="new_note"),
]