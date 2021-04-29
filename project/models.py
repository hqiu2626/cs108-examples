from django.db import models
from django.urls import reverse
import math as math

# Create your models here.

class Chef(models.Model):
    '''Represents a Chef '''

    # data attributes:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField()
    profile_image_url = models.URLField(blank=True)
    price_per_day_of_service = models.IntegerField()


    def __str__(self):
        '''Return a string representation of this chef's profile.'''

        return f'{self.first_name} {self.last_name}' # representation for Chef in admin database

    def get_recipes(self):
        '''Return all recipes for this Chef.'''

        # use the object manager to filter recipes by this chef's pk:
        return Recipe.objects.filter(chef=self)

    def get_bookings(self):
        '''Return all Bookings for this Chef.'''

        # use the object manager to filter recipes by this chef's pk:
        return Booking.objects.filter(chef=self)

    def get_reviews(self):
        '''Return all Reviews for this Chef.'''

        # use the object manager to filter recipes by this chef's pk:
        return Review.objects.filter(chef=self)

    def get_ratings(self):
        '''Return average of ratings for this chef'''

        r = Review.objects.filter(chef=self)
        total_rating = 0
        stars = ""

        for i in r:
            total_rating += int(i.rating)

        if Review.objects.filter(chef=self).count() > 0:
            avg = math.ceil(total_rating/(Review.objects.filter(chef=self).count()))
        else:
            avg = 0

        for i in range(avg):
            stars += "☆"

        return stars


    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        #'quote/<int:pk>'
        return reverse('show_chef_page', kwargs={'pk':self.pk})


class Recipe(models.Model):
    ''' Represents individual recipes for each chef '''

    name = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    prep_time = models.CharField(max_length=50)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    image = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this profile.'''

        return f'{self.chef} - {self.name}' # representation for recipe in admin database

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        #'quote/<int:pk>'
        return reverse('show_chef_page', kwargs={'pk':self.chef.pk})


class Customer(models.Model):
    '''Represents a Customer '''

    # data attributes:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField()
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this Customer.'''

        return f'{self.first_name} {self.last_name}' # representation for Customer in admin database

    def get_bookings(self):
        '''Return all Bookings from this Customers.'''

        # use the object manager to filter recipes by this chef's pk:
        return Booking.objects.filter(customer=self)

    def get_reviews(self):
        '''Return all Reviews from this Customer.'''

        # use the object manager to filter recipes by this customer's pk:
        return Review.objects.filter(customer=self)

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        #'quote/<int:pk>'
        return reverse('show_customer_page', kwargs={'pk':self.pk})


class Booking(models.Model):
    ''' Represents Customers booking Chefs by leaving an event they need to be catered and the date '''

    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    date = models.CharField(max_length=50)

    def __str__(self):
        '''Return a string representation of Hire model.'''

        return f'Chef: {self.chef} - Customer: {self.customer}' # representation for booking in admin database


    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        #'quote/<int:pk>'
        return reverse('show_chef_page', kwargs={'pk':self.pk})


class Review(models.Model):
    ''' Represents Customers leaving Reviews on Chef's profiles '''

    Ratings = (('5', 5),('4', 4),('3', 3),('2', 2),('1', 1))

    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review = models.TextField(blank=True)
    rating = models.CharField(max_length=1, null=True, choices=Ratings)

    def __str__(self):
        '''Return a string representation of Comment model.'''

        return f'Chef: {self.chef} - Customer: {self.customer}' # representation for review in admin database