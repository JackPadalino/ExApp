from django.urls import path
#from users import views as user_views
#from .views import ProjectDetailView,CommentCreateView
#from .views import ProjectCreateView,ProjectUpdateView,ProjectDeleteView,ProjectDetailView
from users import views
from .views import ProjectListView,ProjectCreateView,ProjectDetailView,ProjectUpdateView,ProjectDeleteView

urlpatterns = [
    path('profile/',views.profile,name='users-profile'),
    path('newproject/',ProjectCreateView.as_view(),name='create-project'),
    path('projects/',ProjectListView.as_view(),name='users-studentprojects'),
    path('projects/<int:pk>/',ProjectDetailView.as_view(),name='project-details'),
    path('projects/<int:pk>/update/',ProjectUpdateView.as_view(),name='update-project'),
    path('projects/<int:pk>/delete/',ProjectDeleteView.as_view(),name='delete-project'),
    #path('projects/<int:profile_id>/comment/',CommentCreateView,name='add-comment'),
    #path('projects/<int:user_id>/comment/',CommentCreateView.as_view(),name='add-comment'),
]