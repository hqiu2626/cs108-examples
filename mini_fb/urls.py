# mini_fb/urls.py

from django.urls import path
from .views import * # our view class definition

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"), # path for default url for profile
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"), # path for  url for profile pk
    path('create_profile', CreateProfileView.as_view(), name="create_profile"), # path for creating a new profile
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"), # path for updating a profile
    path('profile/<int:pk>/post_status', post_status_message, name="post_status_message"), # path for posting status
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_status"), # path for deleting status
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name="news_feed"),
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name="show_possible_friends"),
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name="add_friend"),

]