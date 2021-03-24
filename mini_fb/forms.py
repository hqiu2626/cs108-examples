from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new Profile object.'''

    #first_name = forms.CharField(label="First Name", required=True)
    #birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)

    class Meta:
        '''additional data about this form'''

        model = Profile # which model to create
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_image_url'] # which fields to create


class UpdateProfileForm(forms.ModelForm):
    '''A form to update a new Profile object.'''

    #first_name = forms.CharField(label="First Name", required=True)
    #birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)

    class Meta:
        '''additional data about this form'''

        model = Profile # which model to create
        fields = ['city', 'email_address', 'profile_image_url'] # which fields to update

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create a Status object'''

    class Meta:
        '''additional data about this form'''

        model = StatusMessage # which model to create
        fields = ['message'] # which fields to update