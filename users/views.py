from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/login.html',context)

def register(request):
    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

    #context = {
    #    'title':'Register',
    #}
    #return render(request,'users/register.html',context)