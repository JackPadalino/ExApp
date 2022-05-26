from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    periods = [
        ('',''),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('6','6'),
        ('7','7'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    period = models.CharField(max_length=1,choices=periods,default='')

    #project_pics = 

    def __str__(self):
        return f'{self.user.username}'