from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    #image(s) = need to add an image field here for single or multiple project photos
    title = models.CharField(max_length=50)
    blurb = models.CharField(max_length=100,default='Check out my project!')
    description = models.TextField()
    student = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.student.email}'