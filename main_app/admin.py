from django.contrib import admin
from .models import Post, Bid, Crypto, Photo

# Register your models here.
admin.site.register(Post)

admin.site.register(Bid)

admin.site.register(Crypto)

admin.site.register(Photo)
