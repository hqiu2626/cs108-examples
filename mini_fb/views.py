from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Show a listing of Profiles.'''
    model = Profile # retrieve Profile objects from the databse
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"


class ShowProfilePageView(DetailView):
    ''' Obtain data for one Profile record '''
    model = Profile # retrieve Quote objects from the database
    template_name = "mini_fb/show_profile_page.html" # delegate the display to this template
    context_object_name = "profile" # use this variable name in the template
