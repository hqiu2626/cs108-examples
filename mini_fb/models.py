from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    '''Represents a profile '''

    # data attributes:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    profile_image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        '''Return a string representation of this profile.'''

        return f'{self.first_name} {self.last_name}' # representation for profile in admin database
    
    def get_status_messages(self):
        '''Return all statuses for this Person.'''

        # use the object manager to filter statuses by this person's pk:
        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        #'quote/<int:pk>'
        return reverse('show_profile_page', kwargs={'pk':self.pk})

    def get_friends(self):
        ''' return all friends for this Profile '''
        return self.friends.all()

class StatusMessage(models.Model):
    ''' Represents status messages '''

    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True) # an actual image

    def __str__(self):
        '''Return a string representation of this profile.'''

        return f'{self.timestamp} - {self.message} - {self.profile}' # representation for status in admin database





