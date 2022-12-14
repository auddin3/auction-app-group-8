from django.urls import path

from . import views
from auctionapp.views import profile_api

app_name = 'auctionapp'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('user', views.session_api, name="get_userid"),
    path('signup', views.signup, name='signup'),
    path('api/profile/<int:user_id>/', profile_api, name="profile api"),
    path('api/picture/<int:user_id>/', views.picture_api),
    path('api/productPic/', views.productPicture),
    path('api/products/', views.fetch_products, name='fetch_products'),
    ## path('api/products/<int:product_id>/', views.fetch_products_id, name='fetch_product_id'),
    path('api/items/<int:user_id>', views.product_details, name='product_details'),
    ## path('api/search/', api.api_search, name='api_search'),
    path('api/comments/<int:product_id>', views.comment_api),
    path('api/bids/<int:product_id>', views.bid_api),
    path('api/bidCount/<int:product_id>', views.bidCount),
    path('api/logout/<int:user_id>', views.logoutUser, name="logout")
]