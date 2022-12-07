from django.urls import path

from . import views, api

app_name = 'auctionapp'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('api/products/', views.fetch_products, name='fetch_products'),
    path('api/search/', api.api_search, name='api_search'),
    path('auctions', views.search, name='search'),
]