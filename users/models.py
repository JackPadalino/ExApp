from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    period = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)


#TRY THIS
#https://stackoverflow.com/questions/57918725/how-to-extend-django-usercreationform-model-to-include-phone-number-field