from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Represents a profile '''

    # data attributes:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this profile.'''

        return f'{self.first_name} {self.last_name}' # representation for profile in admin database
    
    def get_status_messages(self):
        '''Return all statuses for this Person.'''

        # use the object manager to filter statuses by this person's pk:
        return StatusMessage.objects.filter(profile=self)

class StatusMessage(models.Model):
    ''' Represents status messages '''

    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this profile.'''

        return f'{self.timestamp} - {self.message} - {self.profile}' # representation for status in admin database





