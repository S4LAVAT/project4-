from django.urls import path 
from .views import blog_list, blog_create, blog_filtered, blog_list_ajax


urlpatterns = [ 
    path('blogs', blog_list, name = 'blog_list'),
    path('blogs/new', blog_create, name = 'blog_create'),
    path('blogs_filtered', blog_filtered, name = 'blog_filtered'),
    path('blogs-ajax', blog_list_ajax, name = 'blog_list_ajax')

]
