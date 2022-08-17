from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bids/userbids', views.user_bids, name='user_bids'),
    path('bids/', views.post_list, name='post_list'),
    path('bids/create/', views.PostCreate.as_view(), name='post_create'),
    # path('bids/create/buyer/', views.add_buyer, name='new_buyer'),
    path('bids/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('bids/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('bids/<int:sell_id>/', views.post_detail, name='post_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('bids/<int:sell_id>/new_buyer/', views.add_bid, name='new_buyer'),
]