from multiprocessing import context                        
from django.shortcutsimport render
	def login_page(request):

		context = {}
		return render (request, 'users/login_page.html', context )




