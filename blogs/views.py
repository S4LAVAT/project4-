from contextvars import Context
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import BlogForm
from .filters import BlogFilter
def blog_list(request):
    ordering = request.GET.get('ordering', '-id')
    blogs = Blog.objects.all()
    q = request.GET.get('q' , '')
    q_user = request.GET.get('q_user' , '')
    paginator = Paginator(blogs, 3)
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



def list_blogs(request):
	blogs = Todo.objects.all().order_by('-id')
	q = request.GET.get('q', '')
	# получаем номер страницы на которую юзер хочет посмотреть
	page_number = request.GET.get('page')
	# если при этом есть поиск
	if q:
	# то отфильтруем
		orders = orders.filter(Q(title__icontains=q) | Q(assignee__name__icontains=q))
	# создаем объект Paginator и берем данные по номеру страницы
		paginator = Paginator(blogs, BLOGS_PER_PAGE)
		blogs = paginator.get_page(page_number)
	# дальше стандартный код - контекст и return
	pass

def blog_create(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(reqest.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    context = {'form':form}
    return render(request, 'templates/blogs/blog_create.html')


def blog_filtered(request):
    f  = BlogFilter(request.GET, queryset=Blog.objects.all())
    context= {
        'filter':f
    }
    return render(request, 'blogs/blog_list_filter.html', context)


def blog_list_ajax(request):
    blogs = Blog.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(blogs, 5)
    blogs = paginator.get_page(page_num)
    context={
        'blogs':blogs
    }
    if page_num == 1 or page_num is None:
        return render(request, 'blogs/blog_list_ajax.html', context)
    else:
        return render(request, 'blogs/_blog_list_ajax.html', context)
    
