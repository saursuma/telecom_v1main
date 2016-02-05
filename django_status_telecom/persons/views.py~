from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from persons.models import Persons
from persons.models import Task
from persons.models import Site
from forms import PersonForm
from forms import CommentForm
from forms import SiteForm
from forms import TaskForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.template import RequestContext
from haystack.query import SearchQuerySet
from django.contrib import messages
from persons.models import Comment
from django.utils import timezone
from django.conf import settings



import logging

logr = logging.getLogger(__name__)
# Create your views here.

def persons(request):
	language = 'en-gb'
	session_language = 'en-gb'
	
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	args = {}
	args.update(csrf(request))
	
	args['persons'] = Persons.objects.all()
	args['language'] = language
	args['session_language'] = session_language

	return render_to_response('persons.html', args)

def person(request, person_id=1):
#	return render_to_response('person.html',{'person': Persons.objects.get(id=person_id)},context_instance=RequestContext(request))
#	return render_to_response('person.html',{'person': Persons.objects.get(id=person_id)})
	return render(request,'person.html',{'person': Persons.objects.get(id=person_id)})

def task(request, person_id=1):
	return render_to_response('person.html',{'task': Task.objects.get(id=person_id) })


def language(request, language='en-gb'):
	response = HttpResponse("settings language to %s" % language)

	response.set_cookie('lang', language)

	request.session['lang'] = language
	return response

def create(request):
	#if request.POST:
	if request.method == 'POST':
		form = PersonForm(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Your person added")	
			return HttpResponseRedirect('/persons/all')
	
		else:
			raise Http404
		#else:
		#form = PersonForm()
                
	args = {}
	args.update(csrf(request))
	
	args['form'] = PersonForm()
	print args
	return render_to_response('create_person.html', args)

def delete_comment(request, comment_id):
	c = Comment.objects.get(id=comment_id)
	person_id = c.person.id
	c.delete()
	
	messages.add_message(request, settings.DELETE_MESSAGE, "Your comment was deleted successfully")
	return HttpResponseRedirect('/persons/get/%s' % person_id)

def add_comment(request, person_id):
	a = Persons.objects.get(id=person_id)
	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.CreatedOn = timezone.now()
			c.person = a
			c.save()
	
			messages.success(request, "Your comment was added")
			return HttpResponseRedirect('/persons/get/%s' % person_id)
	else:
		f = CommentForm()
	args = {}
	args.update(csrf(request))
	
	args['person'] = a
	args['form'] = f
	
	return render_to_response('add_comment.html', args)

		
	
	message.add_message(request, settings.DELETE_MESSAGE, "Your comment was deleted successfully")
	return HttpResponseRedirect('/persons/get/%s' % person_id)

def add_site(request):
	
	if request.method == "POST":
		f = SiteForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.CreatedOn = timezone.now()
			c.CreatedBy = request.user
			c.LastUpdatedOn = timezone.now()
			c.LastUpdatedBy = request.user
			
			c.save()
	
			messages.success(request, "Your Site was added")
			return HttpResponseRedirect('/persons/all')
	else:
		f = SiteForm()
	args = {}
	args.update(csrf(request))
	
	
	args['form'] = f
	
	return render_to_response('add_site.html', args)

		
	
	message.add_message(request, settings.DELETE_MESSAGE, "Your site was deleted successfully")
	return HttpResponseRedirect('/persons/all' % person_id)










def like_person(request, person_id):
	if person_id:
		a = Persons.objects.get(id=person_id)
		if a.like >=0:
			count = a.like
			count += 1
		else:
			count=0
			count += 1
		a.like = count
		a.save()
	return HttpResponseRedirect('/persons/get/%s' % person_id)


#def search_titles(request):
#	if request.method == "POST":
#		search_text = request.POST['search_text']

#		logr.debug(search_text)	
#	else:
#		search_text = ''
#	persons = Persons.objects.filter(first_name__contains=search_text)
#	logr.debug(Persons.objects.all())
#	return render_to_response('ajax_search.html', {'persons': persons})

def search_titles(request):
#	persons = Persons.objects.all()
#	persons = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text',''))
        persons = Persons.objects.filter(first_name__icontains=request.POST.get('search_text', ''))
#	sugs = [ person.get_absolute_url() for person in persons]
	
	logr.debug(str(persons))
#	logr.debug(sugs)
	logr.debug(persons.all())
	return render_to_response('ajax_search.html' , {'persons' : persons})

def sites(request):
	
	args = {}
	args.update(csrf(request))
	
	args['sites'] = Site.objects.all()
	

	return render_to_response('sites.html', args)

def tasks(request):
	
	args = {}
	args.update(csrf(request))
	
	args['tasks'] = Task.objects.all()
	

	return render_to_response('tasks.html', args)

 
def create_task(request):
	
	if request.method == "POST":
		f = TaskForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.CreatedOn = timezone.now()
			c.CreatedBy = request.user
			c.LastUpdatedOn = timezone.now()
			c.LastUpdatedBy = request.user
			
			c.save()
	
			messages.success(request, "Your Task was added")
			return HttpResponseRedirect('/persons/all')
	else:
		f = TaskForm()
	args = {}
	args.update(csrf(request))
	
	
	args['form'] = f
	
	return render_to_response('create_task.html', args)

		
	
	message.add_message(request, settings.DELETE_MESSAGE, "Your task was deleted successfully")
	return HttpResponseRedirect('/persons/all' % person_id)

































#def persons(request):
#	name = "Mike"
#	html = "<html> <body> Hi %s, this seems to have worked ! </body></html> " % name 
#	return HttpResponse(html)


#def hello_template(request):
#	name = 'Saurabh'
#	t = get_template('hello.html')
#	html = t.render(Context({'name' : name}))
#	return HttpResponse(html)

#def hello_template_simple(request):
#	name = 'SaurabhSuman'
#	return render_to_response('hello.html' , {'name' : name})

#class HelloTemplate(TemplateView):
	
#	template_name = 'hello_class.html'
	
#	def get_context_data(self, **kwargs):
#		context = super(HelloTemplate, self).get_context_data(**kwargs)
#		context['name'] = 'Mike'
#		return context


