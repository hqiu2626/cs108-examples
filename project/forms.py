from django import forms
from .models import *

class CreateChefForm(forms.ModelForm):
    '''A form to create a new Chef object.'''

    class Meta:
        '''additional data about this form'''

        model = Chef # which model to create
        fields = ['first_name', 'last_name', 'city', 'email_address', 'phone_number', 'profile_image_url', 'price_per_day_of_service'] # which fields to create

class UpdateChefForm(forms.ModelForm):
    '''A form to update a new Chef object.'''

    class Meta:
        '''additional data about this form'''

        model = Chef # which model to update
        fields = ['city', 'email_address', 'phone_number', 'profile_image_url', 'price_per_day_of_service'] # which fields to update

class CreateRecipeForm(forms.ModelForm):
    '''A form to create a Recipe object'''

    class Meta:
        '''additional data about this form'''

        model = Recipe # which model to create
        fields = ['name', 'ingredients', 'instructions', 'prep_time', 'image'] # which fields to create

class UpdateRecipeForm(forms.ModelForm):
    '''A form to update a Recipe object'''

    class Meta:
        '''additional data about this form'''

        model = Recipe # which model to update
        fields = ['name', 'ingredients', 'instructions', 'prep_time', 'image'] # which fields to update


class CreateCustomerForm(forms.ModelForm):
    '''A form to create a Customer object'''

    class Meta:
        '''additional data about this form'''

        model = Customer # which model to create
        fields = ['first_name', 'last_name', 'city', 'email_address', 'phone_number', 'profile_image_url'] # which fields to create


class UpdateCustomerForm(forms.ModelForm):
    '''A form to update a Customer object'''

    class Meta:
        '''additional data about this form'''

        model = Customer # which model to create
        fields = ['first_name', 'last_name', 'city', 'email_address', 'phone_number', 'profile_image_url'] # which fields to create


class CreateBookingForm(forms.ModelForm):
    '''A form to create a Hire object'''

    class Meta:
        '''additional data about this form'''

        model = Booking # which model to create
        fields = ['customer', 'event', 'phone_number', 'date'] # which fields to create



class CreateReviewForm(forms.ModelForm):
    '''A form to create a Review object'''

    class Meta:
        '''additional data about this form'''

        model = Review # which model to create
        fields = ['customer', 'review', 'rating'] # which fields to create

