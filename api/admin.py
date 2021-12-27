from django.contrib import admin

# Register your models here.

from .models import RedditPosts

admin.site.register(RedditPosts)