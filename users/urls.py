from django.urls import path
#from users import views as user_views
#from .views import ProjectDetailView,CommentCreateView
#from .views import ProjectCreateView,ProjectUpdateView,ProjectDeleteView,ProjectDetailView
from users import views
from .views import (
    AllProjectListView,
    FirstPeriodProjectListView,
    SixthPeriodProjectListView,
    SeventhPeriodProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
    MyProjectsListView
)

urlpatterns = [
    path('profile/',views.profile,name='users-profile'),
    path('newproject/',ProjectCreateView.as_view(),name='create-project'),
    path('projects/',AllProjectListView.as_view(),name='users-studentprojects'),

    path('firstperiodprojects/',FirstPeriodProjectListView.as_view(),name='users-firstperiodprojects'),
    path('sixthperiodprojects/',SixthPeriodProjectListView.as_view(),name='users-sixthperiodprojects'),
    path('seventhperiodprojects/',SeventhPeriodProjectListView.as_view(),name='users-seventhperiodprojects'),

    path('myprojects/<int:user_id>/',MyProjectsListView.as_view(),name='users-myprojects'),
    path('projects/<int:pk>/',ProjectDetailView.as_view(),name='project-details'),
    path('projects/<int:pk>/update/',ProjectUpdateView.as_view(),name='update-project'),
    path('projects/<int:pk>/delete/',ProjectDeleteView.as_view(),name='delete-project'),
    #path('projects/<int:profile_id>/comment/',CommentCreateView,name='add-comment'),
    #path('projects/<int:user_id>/comment/',CommentCreateView.as_view(),name='add-comment'),
]