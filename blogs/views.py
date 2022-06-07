from django.shortcuts import render
def blog_list(request):
    return render(requeest, 'blogs/blog_list.html')

def blog_create(request):
    return render(requeest, 'blogs/blog_create.html')
