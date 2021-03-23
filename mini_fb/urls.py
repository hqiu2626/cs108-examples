# mini_fb/urls.py

from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView # our view class definition

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"), # path for default url for profile
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="profile"),
    
]