from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = list(Blog.objects.all())
    return render(request, 'blog/index.html', {'blogs': blogs})
