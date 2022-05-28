from django.urls import path
from users import views as user_views
from .views import ProjectDetailView

urlpatterns = [
    #path('login/',views.login,name='users-login'),
    path('projects/',user_views.displayprojects,name='users-studentprojects'),
    path('profile/',user_views.profile,name='users-profile'),
    path('myproject/',user_views.myproject,name='users-myproject'),
    path('projects/<int:user_pk>/',ProjectDetailView,name='project-details'),
]