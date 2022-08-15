from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Bid(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    time = models.DateTimeField()
    