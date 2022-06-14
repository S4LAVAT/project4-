from contextvars import Context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all().order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blog_list.html', context)




@login_required
def blog_create(request):
    return render(request, 'blogs/blog_create.html')
