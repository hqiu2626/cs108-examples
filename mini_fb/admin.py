from django.contrib import admin

# Register your models here.

from .models import Profile, StatusMessage

admin.site.register(Profile) # register new Profile app
admin.site.register(StatusMessage) # register new StatusMessage

