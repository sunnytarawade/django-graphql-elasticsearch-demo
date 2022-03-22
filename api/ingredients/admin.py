# cookbook/ingredients/admin.py
from django.contrib import admin
from .models import Author, Category, Ingredient, Post

admin.site.register(Category)
admin.site.register(Ingredient)

admin.site.register(Author)
admin.site.register(Post)