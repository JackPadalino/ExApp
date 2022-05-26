from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Profile

# here we are inheriting the user creating form that comes with Django, but we are adding the email field so 
# we can validate a user using their email
class UserRegisterForm(UserCreationForm):
    periods = [
        ('',''),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('6','6'),
        ('7','7'),
    ]
    email = forms.EmailField()
    period = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','period','password1','password2']

# this will create a form that will allow a user to update their profile information
# a model form creates a form that is able to interact with a specific model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

'''
# this will create a form that will alow a user update their profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
'''