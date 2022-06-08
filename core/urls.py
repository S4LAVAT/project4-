
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from users.views import login_page, logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('blogs.urls'))

]
