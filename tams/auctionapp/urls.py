from django.urls import path

from . import views

app_name = 'auctionapp'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('api/profile/<int:user_id>/', profile_api, name="profile api"),
]