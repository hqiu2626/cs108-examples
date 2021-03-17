from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.

class HomePageView(ListView):
    '''Show a listing of Quotes.'''
    model = Profile # retrieve Quote objects from the databse
    template_name = "mini_fb/home.html"
    context_object_name = "profiles"