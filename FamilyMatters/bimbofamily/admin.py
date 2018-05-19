from django.contrib import admin

# Register your models here.
from .models import Author, Category, Quote,Language

admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Language)
