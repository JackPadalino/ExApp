from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Project,Comment,Like#,ProjectVideo,Photo


# Register your models here.
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Like)
#admin.site.register(ProjectVideo)
#admin.site.register(Photo)

'''
# These lines add the profile field to the Django admin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class CommentInline(admin.StackedInline):
    model = Comment
    can_delete = False
    verbose_name_plural = 'comment'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,CommentInLine]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''