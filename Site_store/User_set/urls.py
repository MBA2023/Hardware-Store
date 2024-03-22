from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name="reg"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='users_set/login.html'), name='login'),
    # path("notes/", views.notes, name="notes"),
    # path("add_note/", views.add_note, name="new_note"),
]