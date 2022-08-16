from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bids/userbids', views.user_bids, name='user_bids'),
    path('bids/', views.bid_list, name='bid_index'),
    path('bids/create/', views.BidCreate.as_view(), name='bid_create'),
    path('bids/<int:sell_id>/', views.bid_detail, name='bid_detail'),
    path('accounts/signup/', views.signup, name='signup'),

]