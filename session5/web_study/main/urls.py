from django.urls import path
from .views import *

app_name='main'

urlpatterns=[
    path('',index),
    path('blog/',blog),
    path('blog/<int:pk>/',posting),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]