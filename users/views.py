from multiprocessing import context                        
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm


def login_page(request):
	if reqest.method == 'POST'
		form = AuthenticationForm(reqest, data=reqest.POST)
		if  form.is_valid():
			print("works")
			usermane  = form.clened_data.get('usremane')
			password  = form.clened_data.get('password')
			user = authentical(username = username, password=password)
			if user is not None:
				login(request, user) 
				return redirect('blog_list')
	
	form = AuthenticationForm
	context = {
		'form':form
	}
	return render (request, 'users/login_page.html', context )




