from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Comment,ProjectVideo

# here we are inheriting the user creating form that comes with Django, but we are adding the email field so 
# we can validate a user using their email
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        #fields = ['first_name','last_name','email','username','password1','password2']

class UserProfileForm(forms.ModelForm):
    periods = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (6,6),
        (7,7),
    ]
    period = forms.ChoiceField(choices=periods)

    class Meta:
        model = Profile
        #fields = ['period']
        fields = []

# this will create a form that will allow a user to update their profile information
# a model form creates a form that is able to interact with a specific model
class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()
    #first_name = forms.CharField(max_length=100)
    #last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        #fields = ['first_name','last_name','username','email']
        fields = ['username','email']

# this will create a form that will alow a user update their profile picture
class ProfileUpdateForm(forms.ModelForm):
    periods = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (6,6),
        (7,7),
    ]
    period = forms.ChoiceField(choices=periods)
    class Meta:
        model = Profile
        #fields = ['image']
        fields = []

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProjectVideoForm(forms.ModelForm):
    class Meta:
        model = ProjectVideo
        fields = ['video']