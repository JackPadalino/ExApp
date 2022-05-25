from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login/',views.login,name='users-login'),
    path('login/',auth_views.LoginView.as_view(),name='users-login'),
    path('logou/',auth_views.LogoutView.as_view(),name='users-logout'),
    path('register/',views.register,name='users-register')
]