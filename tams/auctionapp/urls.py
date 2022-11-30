from django.urls import path

from . import views

app_name = 'auctionapp'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('signup.html/', views.signup, name='signup'),
]