from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
#from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from notification.models import Notification

import logging
logr = logging.getLogger(__name__)


def home(request):
	return render(request, "hello.html")

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html' , RequestContext(request, c))

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	n = Notification.objects.filter(user=request.user , viewed=False)
	return render_to_response('loggedin.html',{'full_name': request.user.username, 'notification' :n})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html', {'full_name': request.user.username})

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	
	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	logr.debug(args)
	#print args

	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')



class ContactWizard(SessionWizardView):
	template_name="contact_form.html"
	
	def done(self, form_list, **kwargs):
		form_data = process_form_data(form_list)
				
		return render_to_response("done.html" , {'form_data' : form_data})

def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]

	logr.debug(form_data[0]['subject'])
	logr.debug(form_data[1]['sender'])
	logr.debug(form_data[2]['message'])
	
	send_mail(form_data[0]['subject'] , form_data[2]['message'], form_data[1]['sender'],['saurabh888blue@gmail.com','connect.saurabhsuman@gmail.com'], fail_silently=False)
