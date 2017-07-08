from django.contrib import admin
from .models import Post                # Incluimos o modelo Post de models.py

admin.site.register(Post)
