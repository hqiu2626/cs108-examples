from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Show a listing of Profiles.'''
    model = Profile # retrieve Profile objects from the databse
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"