
from django.urls import path
from users.views import login_page, logout_page, register_page, account_register

urlpatterns = [
    path ('login', login_page , name = "login_page"), 
    path ('logout', logout_page, name = "logout_page"),
    path ('register/', register_page, name = "register_page"),
    path ('account_register', account_register, name = "account_register")
]
