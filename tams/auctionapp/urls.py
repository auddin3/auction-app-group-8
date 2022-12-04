from django.urls import path

from . import views

app_name = 'auctionapp'
urlpatterns = [
    #path('', views.index, name='index'),
    path('login.html/', views.loginUser, name='login'),
    path('signup.html/', views.signup, name='signup'),
]