from django.http import HttpResponse
from django.shortcuts import render

studentprojects = [
    {
        'student':'John',
        'project':"John's project",
        'description':'This will be the best project in the world!'
    },
    {
        'student':'Aylin',
        'project':"Alyin's project",
        'description':'Operation change the world.'
    },
    {
        'student':'Brian',
        'project':"Brian's project",
        'description':"I'm here to make a difference!"
    },
]

# Create your views here.
def displayprojects(request):
    context = {
        'title':'Projects',
        'studentprojects':studentprojects
    }
    return render(request,'projects/studentprojects.html',context)