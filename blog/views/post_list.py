from django.shortcuts import render
from blog.models import *

def post_list(request):
    context = {}
    context['posts'] = Posts.objects.all()
    return render(request, 'blog/post_list.html', context)