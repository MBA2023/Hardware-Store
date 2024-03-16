from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name="reg"),
    path('login/', views.user_login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("notes/", views.notes, name="notes"),
    # path("add_note/", views.add_note, name="new_note"),
]