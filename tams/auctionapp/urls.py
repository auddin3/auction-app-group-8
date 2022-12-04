from django.urls import path

from . import views
from auctionapp.views import profile_api
app_name = 'auctionapp'
urlpatterns = [
     path('api/profile/<int:user_id>/', profile_api, name="profile api"),
]