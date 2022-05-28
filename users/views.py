from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import re
import os

EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN')

# Create your views here.
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/login.html',context)

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

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated.')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title':'My profile',
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)

'''
def period(request):
    if request.method == "POST":
        form = UserPeriodForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account created! You are now able to sign in.')
            return redirect('users-login')
    else:
        form = UserPeriodForm(instance=request.user.profile)  
    context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/period.html',context)
'''

'''
def register(request):
    if request.method=='POST' and request.user is None:
        u_form = UserRegisterForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            email = u_form.cleaned_data.get('email')
            email_domain = re.search("@[\w.]+", email)
            if email_domain.group() == EMAIL_DOMAIN:
                u_form.save()
                p_form.save()
                username = u_form.cleaned_data.get('username')
                messages.success(request,f'Account created for {username}! You are now able to sign in.')
                return redirect('users-login')
            else:
                messages.error(request,f'Sorry. You are not authorized to register.')
    else:       
        u_form = UserRegisterForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)     
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
'''