from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name="reg"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name='logout'),
]