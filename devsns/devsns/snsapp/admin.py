from django.contrib import admin
from .models import FreeComment, Post, Comment, FreePost

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)

# Register your models here.
