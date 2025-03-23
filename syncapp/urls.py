from django.urls import path
from .views import get_facebook_post

urlpatterns = [
    path('api/facebook/', get_facebook_post, name="get_facebook_post"),
]
