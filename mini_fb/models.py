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

