from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Post, Comment, FreeComment, FreePost

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)

# Register your models here.
