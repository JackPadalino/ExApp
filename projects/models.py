from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    blurb = models.CharField(max_length=100,default='Check out my project!')
    description = models.TextField()
    student = models.ForeignKey(User,on_delete=models.CASCADE)