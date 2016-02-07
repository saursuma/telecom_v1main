from django.conf.urls import patterns, url

#urlpatterns = patterns('',
#		url(r'^show/(?P<notification_id\d+)/$', #'notification.views.show_notification'),
#		url(r'^delete/(?P<notification_id\d+)/$', 'notification.views.delete_notification'),
#		url(r'^add_comment/(?P<person_id>\d+)/$', 'persons.views.add_comment'),
#)


urlpatterns = patterns('notification.views',
	url(r'^show/(?P<notification_id>\d+)/$', 'show_notification'),
	url(r'^delete/(?P<notification_id>\d+)/$', 'delete_notification'),
#	url(r'^add_comment/(?P<person_id>\d+)/$', 'persons.views.add_comment'),
#	url(r'^delete_comment/(?P<comment_id>\d+)/$', 'persons.views.delete_comment'),
#	url(r'^search/$', 'persons.views.search_titles'),
#	url(r'^api/', include(person_resource.urls)),
)


	

