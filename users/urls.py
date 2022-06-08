
from django.urls import path
from users.views import login_page, logout_page

urlpatterns = [
    path ('login', login_page , name = "login_page"), 
    path ('logout', logout_page, name = "logout_page")
]


