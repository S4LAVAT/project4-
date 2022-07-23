from django.shortcuts import render
from .models import Profile
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required 
from .forms import UserRegisterForm
from django.contrib.auth import login 
from django.contrib.auth.models import User 

def login_page(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if  form.is_valid():
			print("works")
			username  = form.cleaned_data.get('username')
			password  = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user) 
				return redirect('blog_list')
	
	form = AuthenticationForm()
	context = {
		'form':form
	}
	return render(request, 'users/login_page.html', context )
                      
																																															

def logout_page(request):
	logout(request)
	return redirect('blog_list')


def register_page(request):
	form = UserRegisterForm()
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)    
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False 
			user.save()
			current_site = get_current_site(request)
			subject = 'активация'
			message = render_to_string('users/account_activation.html', { 'user':user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user)})
				
			user.email_user(subject=subject, message=message)
			return redirect('blog_list')

	context = {
		'form':form
	}	

	return render(request, 'users/register_page.html', context)      


@login_required
def me(request):
	return render(request, 'users/me.html')



def account_activation(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoeseNotExist):
		user = None 
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('blog_list')
	else:
		return render (request, 'users/activation_faild.html')





