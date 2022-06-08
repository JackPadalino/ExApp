from django.urls.base import reverse_lazy # this import standard with django
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,CommentForm,ProjectVideoForm,ProjectPhotoForm#,GalleryPhotoForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Project,Comment,Like
import re
import os

EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN')
REGISTERED_EMAILS = os.environ.get('REGISTERED_EMAILS')

# register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            email_domain = re.search("@[\w.]+", email)
            if email_domain.group() == EMAIL_DOMAIN:
            #if email in REGISTERED_EMAILS:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f'Account created for {username}! You are now able to sign in.')
                return redirect('users-login')
            else:
                messages.error(request,f'Sorry. You are not authorized to register.')
    else:
        form = UserRegisterForm()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/register.html',context)





# login view
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/login.html',context)





# list projects view
class AllProjectListView(ListView):
    model = Project
    template_name = 'users/allstudentprojects.html'
    context_object_name = 'projects'





# list projects view
class FirstPeriodProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'users/firstperiodprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        projects = Project.objects.filter(period=1)
        return projects





# list projects view
class SixthPeriodProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'users/sixthperiodprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        projects = Project.objects.filter(period=6)
        return projects





# list projects view
class SeventhPeriodProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'users/seventhperiodprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        projects = Project.objects.filter(period=7)
        return projects





# list projects view
class MyProjectsListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'users/myprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user = get_object_or_404(User,id=self.kwargs.get('user_id'))
        projects = Project.objects.filter(student=user)
        return projects





@login_required
def ProjectDetailView(request,pk):
    user = request.user
    project = Project.objects.get(id=pk)
    comments = Comment.objects.filter(project=project)
    #try:
    #    video = ProjectVideo.objects.get(project=project)
    #except:
    #    video = None
    comment_form = CommentForm()
    if request.method == 'POST':
        if 'commentbutton' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.project = project
                comment.author = user
                comment.save()
                return redirect('project-details',pk=project.pk)
        elif 'likebutton' in request.POST:
            if user in project.liked.all():
                project.liked.remove(user)
            else:
                project.liked.add(user)
            like,created = Like.objects.get_or_create(student=user,project_id=pk)
            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                else:
                    like.value = 'Like'
            like.save()
        else:
            pass
    else:
        comment_form = CommentForm()
    context = {
        'project': project,
        'comments':comments,
        'comment_form':comment_form,
        #'video':video
    }

    return render(request, 'users/project_detail2.html', context)





class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    #fields = ['period','title','blurb','description','video']
    fields = ['period','title','blurb','description']
    
    def form_valid(self,form):
        form.instance.student = self.request.user
        return super().form_valid(form)





class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    #fields = ['period','title','blurb','description','video']
    fields = ['period','title','blurb','description']

    def form_valid(self,form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.student:
            return True
        return False





class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Project
    success_url = reverse_lazy('users-studentprojects')

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.student:
            return True
        return False





# profile details/update view
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,f'Your account information has been updated.')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'title':'My profile',
        'u_form':u_form,
    }
    return render(request,'users/profile.html',context)





@login_required
def CommentCreateView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.author = request.user
            comment.save()
            return redirect('project-details',pk=project.pk)
    else:
        form = CommentForm()
    context = {
        'form':form,
        'project':project
    }
    return render(request,'users/addcomment.html',context)





'''
@login_required
def MediaUpdateView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        p_form = ProjectPhotoVideoForm(request.POST,request.FILES, instance=project)
        if p_form.is_valid():
            p_form.save()
            return redirect('project-details',pk=project.pk)
    else:
        p_form = ProjectPhotoVideoForm(instance=project)
    context = {
        'title':'Add Media',
        'p_form':p_form,
        'project':project
    }
    return render(request,'users/media_form.html',context)
'''





@login_required
def AddPhotoView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectPhotoForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-details',pk=project.pk)
    else:
        form = ProjectPhotoForm(instance=project)
    context = {
        'title':'Add Photo',
        'form':form,
        'project':project
    }
    return render(request,'users/add_photo.html',context)





@login_required
def AddVideoView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = ProjectVideoForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-details',pk=project.pk)
    else:
        form = ProjectVideoForm(instance=project)
    context = {
        'title':'Add Video',
        'form':form,
        'project':project
    }
    return render(request,'users/add_video.html',context)




'''
@login_required
def AddGalleryView(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if request.method == 'POST':
        form = GalleryPhotoForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-details',pk=project.pk)
    else:
        form = GalleryPhotoForm(instance=project)
    context = {
        'title':'Add Gallery Photos',
        'form':form,
        'project':project
    }
    return render(request,'users/add_gallery.html',context)
'''