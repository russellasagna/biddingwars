from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

OPTIONS = (('I', 'Item'), ('J', 'Job'))

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    qr_code = models.TextField()
    type = models.CharField(
        max_length=1,
        choices=OPTIONS,
        default=[0][0]
    )
    ship = models.BooleanField('Ship Item')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'sell_id': self.id})

class Bid(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})

    class Meta: 
        ordering = ['-amount']

class Crypto(models.Model):
    wallet_id = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)