from django.urls.base import reverse_lazy # this import standard with django
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm#,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Project#,Comment
import re
import os

EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN')

# register view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            email_domain = re.search("@[\w.]+", email)
            if email_domain.group() == EMAIL_DOMAIN:
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
class ProjectListView(ListView):
    model = Project
    template_name = 'users/studentprojects.html'
    context_object_name = 'projects'

# list projects view
class MyProjectsListView(ListView):
    model = Project
    template_name = 'users/myprojects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user = get_object_or_404(User,id=self.kwargs.get('user_id'))
        projects = Project.objects.filter(student=user)
        return projects






















class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['period','title','blurb','description']
    
    def form_valid(self,form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
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
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'title':'My profile',
        'u_form':u_form,
    }
    return render(request,'users/profile.html',context)

'''
# other students' project details view
@login_required
def ProjectDetailView(request,project_id):
    project = Project.objects.get(id=project_id)

    #comments = Comment.objects.filter(profile=profile)

    context = {
        'project': project,
        #'comments':comments
    }

    return render(request, 'users/projectdetails.html', context)
'''

'''
@login_required
def CommentCreateView(request,profile_id):
    comment = None
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = Profile.objects.get(id=profile_id)
            comment.author = User.objects.get(id=request.user.id)
            comment.save()
            return redirect('users-studentprojects')

        else:
            form = CommentForm()
    context = {
        'title':'Add comment',
        'form':form
    }
    return render(request,'users/addcomment.html',context)
'''


'''
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'users/addcomment.html'
    form_class=CommentForm
    
    
    def form_valid(self,form):
        form.instance.profile_id = self.kwargs['id']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project-details', kwargs={'id': self.kwargs['id']})
'''

'''
# add comment view
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'blog/add_comment.html'
    form_class=CommentForm

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.kwargs['pk']})
'''