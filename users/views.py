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
	form =  RegistrationForm()
	if request.method == "POST" :
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog_list')
	context = {'form' : form }
	return render(request, 'users/register_page.html', context) 

@login_required
def me(request):
	return render(request, 'users/me.html')


def account_register(request):
	reg_form = UserRegisterForm()
	if request.method == 'POST':
		reg_form = UserRegisterForm(request.POST)    
		if reg_form.is_walid():
			user = reg_form.save(commit=False)
			user.is_active = False 
			user.save()
			current_site = get.current_site()
			subject = 'активация'
			message = render_to_string('registration/account_activation.html', { 'user':user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(forse_butes(user.pk)),
				'token': account_activation_token.make_token(user)})
				
			user.email_user(subject=subject, message=message)
			return redirect('blog_list')

	context = {
		'reg_form':reg_form
	}	

	return render(request, 'users/account_activation.html', context)      

