from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    # path('', blog, name='blog'),
    path('post-list/', post_list, name='post_list'),
    # path('', post_detail, name='post-detail'),
]