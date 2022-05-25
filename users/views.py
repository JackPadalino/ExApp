from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/login.html',context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('users-login')
    else:
        form = UserCreationForm()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/register.html',context)