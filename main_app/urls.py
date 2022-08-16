from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bids/', views.ListCreate.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),

]