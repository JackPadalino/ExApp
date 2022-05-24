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
    if request.metho == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request,'users/register.html',context)

    #context = {
    #    'title':'Register',
    #}
    #return render(request,'users/register.html',context)