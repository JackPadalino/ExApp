from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    context = {
        'title':'My profile'
    }
    return render(request,'users/profile.html',context)