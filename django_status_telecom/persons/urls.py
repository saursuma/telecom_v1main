from django.conf.urls import patterns, include, url
from api import PersonResource

person_resource = PersonResource()
urlpatterns = patterns('',
	url(r'^all/$', 'persons.views.persons'),
	url(r'^all/sites/$', 'persons.views.sites'),
	url(r'^all/tasks/$', 'persons.views.tasks'),
	url(r'^create/task/$', 'persons.views.create_task'),
	#url(r'^all/$', 'persons.views.taskInPersons'),
	url(r'^get/(?P<person_id>\d+)/$', 'persons.views.person'),
	
	#url(r'^task/(?P<person_id>\d+)/$', 'persons.views.task'),
	url(r'^language/(?P<language>[a-z\-]+)/$', 'persons.views.language'),
	url(r'^create/$', 'persons.views.create'),
    	url(r'^create/site/$', 'persons.views.add_site'),
	url(r'^like/(?P<person_id>\d+)/$', 'persons.views.like_person'),
	url(r'^add_comment/(?P<person_id>\d+)/$', 'persons.views.add_comment'),
	url(r'^delete_comment/(?P<comment_id>\d+)/$', 'persons.views.delete_comment'),
	url(r'^search/$', 'persons.views.search_titles'),
	url(r'^api/', include(person_resource.urls)),
)

