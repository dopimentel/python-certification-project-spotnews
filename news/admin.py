from django.contrib import admin
from news.models import Category, News, User

admin.site.register(Category)
admin.site.register(User)
admin.site.register(News)
