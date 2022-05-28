from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    periods = [
        ('-','-'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('6','6'),
        ('7','7'),
    ]
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    period = models.IntegerField(default=1)
    first_name = models.CharField(max_length=100,default='Home')
    last_name = models.CharField(max_length=100,default='Simpson')

    #project_pics = 

    def __str__(self):
        return f'{self.user.username}'


#TRY THIS
#https://stackoverflow.com/questions/57918725/how-to-extend-django-usercreationform-model-to-include-phone-number-field