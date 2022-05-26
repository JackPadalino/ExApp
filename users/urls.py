from django.urls import path
from users import views as user_views

urlpatterns = [
    #path('login/',views.login,name='users-login'),
    path('profile/',user_views.profile,name='users-profile')
]