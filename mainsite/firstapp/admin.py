from django.contrib import admin
from firstapp.models import People, Article, Comment

# Register your models here.
admin.site.register(People)
admin.site.register(Article)
admin.site.register(Comment)