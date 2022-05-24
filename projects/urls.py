from django.urls import path
from . import views

urlpatterns = [
    path('',views.displayprojects,name='projects-studentprojects')
]