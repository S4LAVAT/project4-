
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.url.static import static 
from user.views import login_page, loout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', login_page , name = "login_page"), 
    path ('logout_page', logout_page name = "logout_page"), 
    path( '', include('blogs.urls'))


]
