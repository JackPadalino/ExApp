from dataclasses import field
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #image = models.ImageField(default='/profile_pics/default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

periods = (
    (1,1),
    (6,6),
    (7,7),
)

class Project(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    period = models.IntegerField(choices=periods,default=1)
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='likes')
    #image(s) = need to add an image field here for single or multiple project photos
    title = models.CharField(max_length=50,default='My EXAP project')
    blurb = models.CharField(max_length=100,default='Check out my project')
    description = models.TextField(default="I haven't written my project description yet, but trust me it will be awesome!")

    def __str__(self):
        return f'{self.title} | {self.student.first_name} {self.student.last_name}'
    
    def get_absolute_url(self):
        return reverse('project-details',kwargs={'pk':self.pk})
    
    @property
    def count_likes(self):
        return self.liked.all().count()

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f'{self.content} | {self.author}'
    
    #def get_absolute_url(self):
    #    return reverse('post-details',kwargs={'pk':self.pk})

like_choices = (
    ('Like','Like'),
    ('Unlike','Unlike') 
)

class Like(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    value = models.CharField(choices=like_choices,default='Like',max_length=10)

    def __str__(self):
        return f'{self.project}'

'''
class Comment(models.Model):
    profile = models.ForeignKey(Profile,related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.content} - {self.author.first_name} {self.author.last_name} on {self.profile.user.first_name} {self.profile.user.last_name}'s project"
'''