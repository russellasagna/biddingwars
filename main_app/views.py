import os
import uuid
import boto3
from pickle import FALSE
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BidForm, SignUp, CryptoForm
from .models import Post, Bid, Crypto, Photo
from django.core.exceptions import ValidationError

def some_function(request):
    secret_key = os.environ['SECRET_KEY']

def home(request):
    return render(request, 'home.html', {})

def user_bids(request):
    my_bids = Post.objects.filter(user=request.user)
    return render(request, 'user_stuff/user_bids.html', {'posts': my_bids})

def post_list(request):
  all_bids = Post.objects.exclude(user=request.user)
  return render(request, 'main_app/post_list.html', {'posts': all_bids})
  

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  buyer_form = BidForm()
  buyer_data = Post.objects.get(id=post_id).bid_set.all()
  return render(request, 'main_app/post_detail.html', { 'post': post ,'form': buyer_form, 'buyer_data': buyer_data})

class PostCreate(CreateView, LoginRequiredMixin):
  model = Post
  fields = ['title','description', 'price', 'type', 'ship']

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.qr_code = Crypto.objects.get(user=self.request.user).wallet_id
    return super().form_valid(form)

class PostUpdate(UpdateView, LoginRequiredMixin):
  model = Post
  fields = ['title','description', 'price', 'type', 'ship']

class PostDelete(DeleteView, LoginRequiredMixin):
  model = Post
  success_url = '/bids/userbids'


def add_bid(request, post_id):
  form = BidForm(request.POST)
  post = Post.objects.get(id=post_id)
  buyer_data = post.bid_set.all()
  user_pay = float(request.POST['amount'])
  if(buyer_data):
    last_buyer = buyer_data.latest('amount')
    if(user_pay <= last_buyer.amount or user_pay < post.price):
      return redirect('post_detail', post_id=post_id)
  elif (user_pay <= post.price):
    return redirect('post_detail', post_id=post_id)


  if form.is_valid():
    new_bid = form.save(commit=False)
    new_bid.name = request.user
    new_bid.post_id = post_id
    new_bid.user_id = request.user.id
    new_bid.save()
    
  return redirect('post_detail', post_id=post_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignUp(request.POST)
    crypto_form = CryptoForm()
      
      
    if form.is_valid():
      user = form.save()
      new_wallet = crypto_form.save(commit=False)
      new_wallet.wallet_id = request.POST['crypto_wallet']
      new_wallet.user_id = user.id
      new_wallet.save()
      
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignUp()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_photo(request, post_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, post_id=post_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('post_detail', post_id=post_id)