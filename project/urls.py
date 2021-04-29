# project/urls.py

from django.urls import path
from .views import * # our view class definition

urlpatterns = [
    path('chefs', ShowAllChefsView.as_view(), name="show_all_chefs"), # path for default url for chef's profile
    path('chef/<int:pk>', ShowChefPageView.as_view(), name="show_chef_page"), # path for  url for chef's profile pk
    path('create_chef', CreateChefView.as_view(), name="create_chef"), # path for creating a new chef profile
    path('chef/<int:pk>/update', UpdateChefView.as_view(), name="update_chef"), # path for updating a chef's profile
    path('chef/<int:pk>/post_recipe', post_recipe, name="post_recipe"), # path for posting recipe
    path('recipe/<int:pk>/update', UpdateRecipeView.as_view(), name="update_recipe"), # path for updating a recipe
    path('chef/<int:chef_pk>/delete_recipe/<int:recipe_pk>', DeleteRecipeView.as_view(), name="delete_recipe"), # path for deleting recipe
    path('customers', ShowAllCustomersView.as_view(), name="show_all_customers"), # path for default url for showing all customeers
    path('customer/<int:pk>', ShowCustomerPageView.as_view(), name="show_customer_page"), # path for  url for customer's profile pk
    path('create_customer', CreateCustomerView.as_view(), name="create_customer"),  #path for updating a customer's profile
    path('customer/<int:pk>/update', UpdateCustomerView.as_view(), name="update_customer"), # path for updating a customer's profile
    path('chef/<int:pk>/post_booking', post_booking, name="post_booking"), # path for posting new booking
    path('chef/<int:chef_pk>/delete_booking/<int:booking_pk>', DeleteBookingView.as_view(), name="delete_booking"), # path for deleting booking
    path('customer/<int:customer_pk>/delete_booking/<int:booking_pk>', DeleteBookingView2.as_view(), name="delete_booking2"), # path for deleting booking
    path('chef/<int:pk>/post_review', post_review, name="post_review"), # path for posting new review
    path('chef/<int:chef_pk>/delete_review/<int:review_pk>', DeleteReviewView.as_view(), name="delete_review"), # path for deleting review
    path('customer/<int:customer_pk>/delete_review/<int:review_pk>', DeleteReviewView2.as_view(), name="delete_review2"), # path for deleting review on customer profile page
    path('log_in', loginemail, name='log_in'), # path for login in chef by email
    path('', loginemailcustomer, name='log_in_customer'), # path for login in customer by email
]