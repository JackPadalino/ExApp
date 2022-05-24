from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title':'Login',
    }
    return render(request,'users/login.html',context)

def register(request):
    context = {
        'title':'Register',
    }
    return render(request,'users/register.html',context)