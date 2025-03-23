from django.urls import path
from .views import get_facebook_post, post_to_twitter_api, post_to_linkedin_api

urlpatterns = [
    path('api/facebook/', get_facebook_post, name="get_facebook_post"),
    path('api/twitter/', post_to_twitter_api, name="post_to_twitter"),
    path('api/linkedin/', post_to_linkedin_api, name="post_to_linkedin"),
]
