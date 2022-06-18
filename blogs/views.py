from contextvars import Context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator



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


def list_blog(request):
	todos = Blogs.objects.all().order_by('-id')
	q = request.GET.get('q', '')
	# получаем номер страницы на которую юзер хочет посмотреть
  page_number = request.GET.get('page')
	# если при этом есть поиск
  if q:
	# то отфильтруем
	  orders = orders.filter(Q(title__icontains=q) | Q(assignee__name__icontains=q))
	# создаем объект Paginator и берем данные по номеру страницы
	paginator = Paginator(todos, TODOS_PER_PAGE)
	todos = paginator.get_page(page_number)
	# дальше стандартный код - контекст и return
    return render(request, 'pagination3.html')
