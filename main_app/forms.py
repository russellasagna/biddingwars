from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Bid, Crypto

class BidForm(ModelForm):
  class Meta:
    model = Bid
    fields = ['amount']

class SignUp(UserCreationForm):
  model = User 
  crypto_wallet = forms.CharField(max_length=None)
  fields = '__all__'

class CryptoForm(ModelForm):
  class Meta:
    model = Crypto
    fields = '__all__'