from django.contrib import admin
from .models import Comment, Post , Categories , Profile

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Profile)
admin.site.register(Comment)