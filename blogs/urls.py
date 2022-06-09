from django.urls import path 
from .views import blog_list, blog_create

urlpatterns = [ 
    path('blogs', blog_list, name = 'blog_list'),
    path('blogs/new', blog_create, name = 'blog_create'),
]
