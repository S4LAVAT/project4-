from django.urls import path 
from .views import blog_list, blog_create, blog_list_pagination


urlpatterns = [ 
    path('blogs', blog_list, name = 'blog_list'),
    path('blogs/new', blog_create, name = 'blog_create'),
    path('blog_list_pagination', blog_list_pagination, name = 'blog_list_pagination'),
   

]
