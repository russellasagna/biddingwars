from django.urls import path
from . import viewsMyFile

urlpatterns = [
    path('', viewsMyFile.home, name='home'),
    path('bids/userbids', viewsMyFile.user_bids, name='user_bids'),
    path('bids/', viewsMyFile.post_list, name='post_list'),
    path('bids/create/', viewsMyFile.PostCreate.as_view(), name='post_create'),
    # path('bids/create/buyer/', views.add_buyer, name='new_buyer'),
    path('bids/<int:pk>/update/', viewsMyFile.PostUpdate.as_view(), name='post_update'),
    path('bids/<int:pk>/delete/', viewsMyFile.PostDelete.as_view(), name='post_delete'),
    path('bids/<int:sell_id>/', viewsMyFile.post_detail, name='post_detail'),
    path('accounts/signup/', viewsMyFile.signup, name='signup'),
    path('bids/<int:sell_id>/new_buyer/', viewsMyFile.add_bid, name='new_buyer'),
]