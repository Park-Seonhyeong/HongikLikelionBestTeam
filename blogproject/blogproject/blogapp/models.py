from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
import tkinter as Tk
from tkinter import Tk


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임
    # blog객체 참조하는 foreign 키로 만들어줘야함
    #CASCADE이부분은 참조하는 대상이 삭제되면 얘도 삭제하라는 뜻
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment