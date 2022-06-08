from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Project,Comment,Like#,GalleryPhoto

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Like)
#admin.site.register(GalleryPhoto)