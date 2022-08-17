from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BidForm
from .models import Post, Bid

# Create your views here.

def home(request):
    # all_bids = Post.object.all()
    return render(request, 'home.html', {
      # 'bids': all_bids,
    })

def user_bids(request):
    my_bids = Post.objects.filter(user=request.user)
    return render(request, 'user_stuff/user_bids.html', {'posts': my_bids})

def post_list(request):
  all_bids = Post.objects.exclude(user=request.user)
  buyer_form = BidForm()
  return render(request, 'main_app/post_list.html', {'posts': all_bids, 'form': buyer_form})
  

def post_detail(request, sell_id):
  post = Post.objects.get(id=sell_id)
  return render(request, 'main_app/post_detail.html', { 'post': post })

class PostCreate(CreateView, LoginRequiredMixin):
  model = Post
  fields = ['title','description', 'price', 'type', 'ship']
  # success_url = '/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    # Let the CreateView superclass do its usual job
    return super().form_valid(form)

class PostUpdate(UpdateView, LoginRequiredMixin):
  model = Post
  fields = ['title','description', 'price', 'type', 'ship']
  # success_url = '/'

class PostDelete(DeleteView, LoginRequiredMixin):
  model = Post
  success_url = '/bids/'


def add_bid(request, sell_id):
  form = BidForm(request.POST)
  if form.is_valid():
    new_bid = form.save(commit=False)
    new_bid.post_id = sell_id
    new_bid.user_id = request.user.id
    new_bid.save()
  
  return redirect('post_detail', sell_id=sell_id)

# def add_buyer(request, sell_id)

# class BuyerCreate()
# create new buyer 

# if not owner of listing

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
