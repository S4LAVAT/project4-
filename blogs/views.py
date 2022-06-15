from contextvars import Context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog
from django.db.models import Q


def blog_list(request):
    ordering = request.GET.get('ordering', '-id')
    blogs = Blog.objects.all()
    q = request.GET.get('q' , '')
    q_user = request.GET.get('q_user' , '')
    if q or q_user:
        blogs = Blog.objects.filter((Q(title__icontains=q) | Q(text__icontains=q)) &  Q(author__username__icontains=q_user)).distinct()
    elif ordering == 'id':
        blogs = blogs.order_by('id')
        ordering  = '-id'
    else:
        blogs = blogs.order_by('id')
        ordering  = '-id'
    context={
        'blogs':blogs,
        'ordering':ordering,
        'q':q,
        'q_user':q_user
    }   
    return render(request, 'blogs/blog_list.html', context)


@login_required
def blog_create(request):
    return render(request, 'blogs/blog_create.html')
