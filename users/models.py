from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    period = models.IntegerField(default=1)
    #image(s) = need to add an image field here for single or multiple project photos
    project_title = models.CharField(max_length=50,default='My EXAP project')
    project_blurb = models.CharField(max_length=100,default='Check out my project!')
    project_description = models.TextField(default="I don't have a project description yet, but trust me it will be awesome!")

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


#TRY THIS
#https://stackoverflow.com/questions/57918725/how-to-extend-django-usercreationform-model-to-include-phone-number-field