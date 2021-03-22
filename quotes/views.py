from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote
import random

# Create your views here.

class HomePageView(ListView):
    '''Show a listing of Quotes.'''
    model = Quote # retrieve Quote objects from the databse
    template_name = "quotes/home.html" # delegate the display to this template
    context_object_name = "quotes" # use this variable namee in the template

class QuotePageView(DetailView):
    ''' Display a single quote object. '''
    model = Quote # retrieve Quote objects from the databasee
    template_name = "quotes/quote.html" # delegate the display to this template
    context_object_name = "quote" # use this variable namee in the template

class RandomQuotePageView(DetailView):
    ''' Display a single quote object. '''
    model = Quote # retrieve Quote objects from the databasee
    template_name = "quotes/quote.html" # delegate the display to this template
    context_object_name = "quote" # use this variable namee in the template

    def get_object(self):
        ''' Select one quote at random for display in the quote.html template. '''

        # obtain all quotes using the object manager
        quotes = Quote.objects.all()

        #select one at random
        q = random.choice(quotes)
        return q