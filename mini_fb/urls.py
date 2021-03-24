# mini_fb/urls.py

from django.urls import path
from .views import * # our view class definition

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"), # path for default url for profile
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"), # path for  url for profile pk
    path('create_profile', CreateProfileView.as_view(), name="create_profile"), # path for creating a new profile
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"), # path for updating a profile
    path('profile/<int:pk>/post_status', post_status_message, name="post_status_message"), # path for posting status
]