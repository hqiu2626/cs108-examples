from django.contrib import admin

# Register your models here.

from .models import Chef, Recipe, Customer, Booking, Review

admin.site.register(Chef) # register new Chef app
admin.site.register(Recipe) # register new Recipe app
admin.site.register(Customer) # register new Customer app
admin.site.register(Booking) # register new Hire app
admin.site.register(Review) # register new Review app

