"""Django admin config for blog app."""
from django.contrib import admin
from .models import Post

admin.site.register(Post)
