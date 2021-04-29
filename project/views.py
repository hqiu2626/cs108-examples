from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.shortcuts import redirect
from django.urls import reverse
from project.forms import *

# Create your views here.

class ShowAllChefsView(ListView):
    '''Show a listing of Chef.'''
    model = Chef # retrieve Chef objects from the databse
    template_name = "project/show_all_chefs.html"
    context_object_name = "chefs"


class ShowChefPageView(DetailView):
    ''' Obtain data for one Recipe record '''
    model = Chef # retrieve Chef objects from the database
    template_name = "project/show_chef_page.html" # delegate the display to this template
    context_object_name = "chef" # use this variable name in the template

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowChefPageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateRecipeForm() 
        form1 = CreateBookingForm()
        form2 = CreateReviewForm()
        context['create_recipe_form'] = form
        context['create_booking_form'] = form1
        context['create_review_form'] = form2
        # return this context dictionary
        return context


class CreateChefView(CreateView):
    ''' Create a new Chef object and store it in the database. '''

    model = Chef # which model to create
    form_class = CreateChefForm
    template_name = "project/create_chef_form.html" #delegate the display to this template

class UpdateChefView(UpdateView):
    ''' Create a new Chef object and store it in the database. '''

    model = Chef # which model to create
    form_class = UpdateChefForm
    template_name = "project/update_chef_form.html" #delegate the display to this template


class UpdateRecipeView(UpdateView):
    ''' Update a new Recipe object and store it in the database. '''

    model = Recipe # which model to create
    form_class = UpdateRecipeForm
    template_name = "project/update_recipe_form.html" #delegate the display to this template


class ShowAllCustomersView(ListView):
    '''Show a listing of Customer.'''
    model = Customer # retrieve Customer objects from the databse
    template_name = "project/show_all_customers.html"
    context_object_name = "customers"


class ShowCustomerPageView(DetailView):
    ''' Obtain data for one Recipe record '''
    model = Customer # retrieve Chef objects from the database
    template_name = "project/show_customer_page.html" # delegate the display to this template
    context_object_name = "customer" # use this variable name in the template

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowCustomerPageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateRecipeForm() 
        form1 = CreateBookingForm()
        form2 = CreateReviewForm()
        context['create_recipe_form'] = form
        context['create_booking_form'] = form1
        context['create_review_form'] = form2
        # return this context dictionary
        return context


class CreateCustomerView(CreateView):
    ''' Create a new Customer object and store it in the database. '''

    model = Customer # which model to create
    form_class = CreateCustomerForm
    template_name = "project/create_customer_form.html" #delegate the display to this template


class UpdateCustomerView(UpdateView):
    ''' Update a new Customer object and store it in the database. '''

    model = Customer # which model to create
    form_class = UpdateCustomerForm
    template_name = "project/update_customer_form.html" #delegate the display to this template


class DeleteRecipeView(DeleteView):
    ''' Delete a new Recipe object'''
    template_name = "project/delete_recipe_form.html"
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        ''' returns the context data in the template '''
        # obtains context data dictionary by callling super class
        context = super(DeleteRecipeView, self).get_context_data(**kwargs)

        # Find the status message object that we are trying to delete, and save it to a variable
        rcpe = Recipe.objects.get(pk=self.kwargs['recipe_pk'])

        # add to the dictionary of context data
        context['rcpe'] = rcpe

        # return context data
        return context

    def get_object(self):
        ''' return Recipe object that should be deleted '''

        # read the URL data values into variables   
        chef_pk = self.kwargs['chef_pk']
        recipe_pk = self.kwargs['recipe_pk']

        # find the Recipe object, and return it
        recipe = Recipe.objects.filter(pk=recipe_pk).first()
        return recipe


    def get_success_url(self):
        ''' where the browser should be directed after delete is complete '''

        # read the URL data values into variables
        chef_pk = self.kwargs['chef_pk']
        recipe_pk = self.kwargs['recipe_pk']

        # reverse to show the Chef page
        return reverse('show_chef_page', kwargs={'pk':chef_pk})

def post_recipe(request, pk):
    '''
    Process a form submission to post a new recipe.
    '''

    chef = Chef.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateRecipeForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            image = form.save(commit=False)
            image.chef = chef
            image.save()


    # redirect the user to the show_profile_page view
    url = reverse('show_chef_page', kwargs={'pk': pk})
    return redirect(url)





class DeleteBookingView(DeleteView):
    ''' Delete a new Recipe object'''
    template_name = "project/delete_booking_form.html"
    queryset = Booking.objects.all()

    def get_context_data(self, **kwargs):
        ''' returns the context data in the template '''
        # obtains context data dictionary by callling super class
        context = super(DeleteBookingView, self).get_context_data(**kwargs)

        # Find the status message object that we are trying to delete, and save it to a variable
        bking = Booking.objects.get(pk=self.kwargs['booking_pk'])

        # add to the dictionary of context data
        context['bking'] = bking

        # return context data
        return context

    def get_object(self):
        ''' return Booking object that should be deleted '''

        # read the URL data values into variables   
        chef_pk = self.kwargs['chef_pk']
        booking_pk = self.kwargs['booking_pk']

        # find the Recipe object, and return it
        booking = Booking.objects.filter(pk=booking_pk).first()
        return booking


    def get_success_url(self):
        ''' where the browser should be directed after delete is complete '''

        # read the URL data values into variables
        chef_pk = self.kwargs['chef_pk']
        booking_pk = self.kwargs['booking_pk']

        # reverse to show the Chef page
        return reverse('show_chef_page', kwargs={'pk':chef_pk})



class DeleteBookingView2(DeleteView):
    ''' Delete a new Recipe object'''
    template_name = "project/delete_booking_form2.html"
    queryset = Booking.objects.all()

    def get_context_data(self, **kwargs):
        ''' returns the context data in the template '''
        # obtains context data dictionary by callling super class
        context = super(DeleteBookingView2, self).get_context_data(**kwargs)

        # Find the status message object that we are trying to delete, and save it to a variable
        bking = Booking.objects.get(pk=self.kwargs['booking_pk'])

        # add to the dictionary of context data
        context['bking'] = bking

        # return context data
        return context

    def get_object(self):
        ''' return Booking object that should be deleted '''

        # read the URL data values into variables   
        customer_pk = self.kwargs['customer_pk']
        booking_pk = self.kwargs['booking_pk']

        # find the Recipe object, and return it
        booking = Booking.objects.filter(pk=booking_pk).first()
        return booking


    def get_success_url(self):
        ''' where the browser should bee directed after delete is complete '''

        # read the URL data values into variables
        customer_pk = self.kwargs['customer_pk']
        booking_pk = self.kwargs['booking_pk']

        # reverse to show the Chef page
        return reverse('show_customer_page', kwargs={'pk':customer_pk})
        


def post_booking(request, pk):
    '''
    Process a form submission to post a new Booking.
    '''

    chef = Chef.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateBookingForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            image = form.save(commit=False)
            image.chef = chef
            image.save()


    # redirect the user to the show_profile_page view
    url = reverse('show_chef_page', kwargs={'pk': pk})
    return redirect(url)





class DeleteReviewView(DeleteView):
    ''' Delete a new Recipe object'''
    template_name = "project/delete_review_form.html"
    queryset = Review.objects.all()

    def get_context_data(self, **kwargs):
        ''' returns the context data in the template '''
        # obtains context data dictionary by callling super class
        context = super(DeleteReviewView, self).get_context_data(**kwargs)

        # Find the status message object that we are trying to delete, and save it to a variable
        rview = Review.objects.get(pk=self.kwargs['review_pk'])

        # add to the dictionary of context data
        context['rview'] = rview

        # return context data
        return context

    def get_object(self):
        ''' return Review object that should be deleted '''

        # read the URL data values into variables   
        chef_pk = self.kwargs['chef_pk']
        review_pk = self.kwargs['review_pk']

        # find the Recipe object, and return it
        review = Review.objects.filter(pk=review_pk).first()
        return review


    def get_success_url(self):
        ''' where the browser should be directed after delete is complete '''

        # read the URL data values into variables
        chef_pk = self.kwargs['chef_pk']
        review_pk = self.kwargs['review_pk']

        # reverse to show the Chef page
        return reverse('show_chef_page', kwargs={'pk':chef_pk})


class DeleteReviewView2(DeleteView):
    ''' Delete a new Recipe object'''
    template_name = "project/delete_review_form2.html"
    queryset = Review.objects.all()

    def get_context_data(self, **kwargs):
        ''' returns the context data in the template '''
        # obtains context data dictionary by callling super class
        context = super(DeleteReviewView2, self).get_context_data(**kwargs)

        # Find the status message object that we are trying to delete, and save it to a variable
        rview = Review.objects.get(pk=self.kwargs['review_pk'])

        # add to the dictionary of context data
        context['rview'] = rview

        # return context data
        return context

    def get_object(self):
        ''' return Review object that should be deleted '''

        # read the URL data values into variables   
        customer_pk = self.kwargs['customer_pk']
        review_pk = self.kwargs['review_pk']

        # find the Recipe object, and return it
        review = Review.objects.filter(pk=review_pk).first()
        return review


    def get_success_url(self):
        ''' where the browser should be directed after delete is complete '''

        # read the URL data values into variables
        customer_pk = self.kwargs['customer_pk']
        review_pk = self.kwargs['review_pk']

        # reverse to show the Chef page
        return reverse('show_customer_page', kwargs={'pk':customer_pk})


def post_review(request, pk):
    '''
    Process a form submission to post a new Booking.
    '''

    chef = Chef.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateReviewForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            image = form.save(commit=False)
            image.chef = chef
            image.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_chef_page', kwargs={'pk': pk})
    return redirect(url)


def loginemail(request):
    ''' Log in chef user method based off email_address'''

    # find the type of method
    if (request.method == 'POST'):
        email_address = request.POST['email_address'] # check if it is an email_address attribute

        # filter based off Chef objects with equivalent email_address
        # email_address is made as a unique attribute field
        chef = Chef.objects.filter(email_address=email_address)

        if (len(chef) != 0):
            pk = chef[0].pk # acquires the first and only customer from the list
            url = reverse('show_chef_page', kwargs={'pk': pk})
            return redirect(url)
            
    return render(request, 'project/log_in.html') # redirects to home page if unsucessful


def loginemailcustomer(request):
    ''' Log in customer user method based off email_address'''

    # find the type of method
    if (request.method == 'POST'):
        email_address = request.POST['email_address'] # check if it is an email_address attribute

        # filter based off Customer objects with equivalent email_address
        # email_address is made as a unique attribute field
        customer = Customer.objects.filter(email_address=email_address)  
        
        if (len(customer) != 0):
            pk = customer[0].pk # acquires the first and only customer from the list

            url = reverse('show_customer_page', kwargs={'pk': pk})
            return redirect(url)
            
    return render(request, 'project/log_in.html') # redirects to home page if unsucessful