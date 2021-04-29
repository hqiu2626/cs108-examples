from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse
from mini_fb.forms import *


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

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    ''' Create a new Profile object and store it in the database. '''

    model = Profile # which model to create
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html" #delegate the display to this template

class UpdateProfileView(UpdateView):
    ''' Create a new Profile object and store it in the database. '''

    model = Profile # which model to create
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html" #delegate the display to this template


class DeleteStatusMessageView(DeleteView):
    ''' Delete a new StatusMessage object'''
    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        ''' returns the context data in the template '''
        # obtains context data dictionary by callling super class
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)

        # Find the status message object that we are trying to delete, and save it to a variable
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])

        # add to the dictionary of context data
        context['st_msg'] = st_msg

        # return context data
        return context

    def get_object(self):
        ''' return StatusMessage object that should be deleted '''

        # read the URL data values into variables   
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        status = StatusMessage.objects.filter(pk=status_pk).first()
        return status


    def get_success_url(self):
        ''' where the browser should bee directed after delete is complete '''

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # reverse to show the profile page
        return reverse('show_profile_page', kwargs={'pk':profile_pk})

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)


        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            #status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            #profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            #status_message.profile = profile

            # now commit to database
            #status_message.save()


            image = form.save(commit=False)
            image.profile = profile
            image.save()


    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)


class ShowNewsFeedView(DetailView):
    ''' displays news feed '''

    model = Profile
    template_name = 'mini_fb/show_news_feed.html'

class ShowPossibleFriendsView(DetailView):
    ''' show possible friends ''' 
    model = Profile
    template_name = 'mini_fb/show_possible_friends.html'


def add_friend(request, profile_pk, friend_pk):
    ''' process the add_friend request, to add a friend for a given profile ''' 

    # find the Profile object which is adding the friend, and store it into a variable
    profile = Profile.objects.get(pk=profile_pk)

    # find the Profile object of the friend to add, and store it into another variable
    friend = Profile.objects.get(pk=friend_pk)

    # add that friend’s Profile into the profile.friends object (using the method add).
    profile.friends.add(friend)

    # save the profile object.
    profile.save()

    return redirect(reverse('show_possible_friends', kwargs={'pk': profile_pk}))