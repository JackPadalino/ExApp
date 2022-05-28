from django.urls.base import reverse_lazy # this import standard with django
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Comment,Profile
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

def displayprojects(request):
    context = {
        'title':'Projects',
        'users':User.objects.all()
    }
    return render(request,'users/studentprojects.html',context)

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

# my project details/update view
@login_required
def myproject(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('users-myproject')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title':'My ExAP',
        'p_form':p_form
    }
    return render(request,'users/myproject.html',context)

# other students' project details view
def ProjectDetailView(request,user_pk):
    user = User.objects.get(pk=user_pk)
    #comments = Comment.objects.filter(profile=profile)

    context = {
        'user': user,
        #'comments':comments
    }

    return render(request, 'users/projectdetails.html', context)

'''
# add comment view
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'users/addcomment.html'
    form_class=CommentForm

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project-details', kwargs={'pk': self.kwargs['pk']})
'''