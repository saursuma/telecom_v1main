from __future__ import unicode_literals

from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.

class Persons(models.Model):
    MANAGER = 'MN'
    ENGINEER= 'EN'
    TECHNICIAN='TE'
    NA='NA'
    ROLE_CHOICES = (
        (MANAGER,'Manager'),
        (ENGINEER,'Engineer'),
        (TECHNICIAN,'Technician'),
        (NA,'Not Assigned'),
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
   # role = models.CharField(max_length=1, choices=(('M', ('Manager')), ('I', ('Developer')))
    email = models.CharField(max_length=254, null=True)
    address = models.CharField(max_length=254, null=True)
    birthdate = models.DateField(null=True)
    city = models.CharField(max_length=60, null=True)
    like = models.IntegerField(null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    CreatedOn = models.DateField(max_length=254, null=True)
    CreatedBy = models.CharField(max_length=254, null=True)
    LastUpdatedOn = models.DateField(max_length=254, null=True)
    LastUpdatedBy = models.CharField(max_length=254, null=True)
    role = models.CharField(max_length=10,
                                      choices=ROLE_CHOICES,
                                      default=NA)
    
    
    
    
    
    def __unicode__(self):
        return self.first_name
#    def __unicode__(self):
#		return self.first_name

#    def get_absolute_url(self):
#        	return "/persons/get/%i/" % self.id
    def get_absolute_url(self):
      return "/persons/get/%i/" % self.id 
    def get_full_name(self):
      return '%s %s' % (self.first_name, self.last_name)      



def __unicode__(self):
		return self.TaskStatus


class Site(models.Model):
    site_id = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=254, null=True)
    description = models.CharField(max_length=254, null=True)
    latitude= models.FloatField(max_length=254, null=True)
    longitude= models.FloatField(max_length=254, null=True)
    CreatedOn = models.DateField(max_length=254, null=True)
    CreatedBy = models.CharField(max_length=254, null=True)
    LastUpdatedOn = models.DateField(max_length=254, null=True)
    LastUpdatedBy = models.CharField(max_length=254, null=True)

 
class Task(models.Model):
	Highest = 'H'
	Medium= 'M'
	Low='L'
	NA='NA'
	PRIORITY_CHOICES = (
         (Highest,'Highest'),
         (Medium,'Medium'),
         (Low,'Low'),
         (NA,'Not Assigned'),
        )
	person = models.ForeignKey(Persons)
        site = models.ForeignKey(Site, default='1')
	description = models.CharField(max_length=254, default='Dummy')
	task_initiator= models.CharField(max_length=254, null=True)
	actual_owner = models.CharField(max_length=254, null=True)
	task_status = models.CharField(max_length=254, null=True)
	task_priority = models.CharField(max_length=10,
                                      choices=PRIORITY_CHOICES,
                                      default=NA)
	CreatedOn = models.CharField(max_length=254, null=True)
	CreatedBy = models.CharField(max_length=254, null=True)
	CompletedOn = models.CharField(max_length=254, null=True)
	CompletedBy = models.CharField(max_length=254, null=True)
	LastUpdatedOn = models.DateField(max_length=254, null=True)
	LastUpdatedBy = models.CharField(max_length=254, null=True)
	task_type = models.CharField(max_length=254, null=True)

class Comment(models.Model):
	person = models.ForeignKey(Persons, default=1)
	task = models.ForeignKey(Task)
	description = models.CharField(max_length=254, null=True)
	CreatedOn = models.CharField(max_length=254, null=True)
	CreatedBy = models.CharField(max_length=254, null=True)
	LastUpdatedOn = models.DateField(max_length=254, null=True)
	LastUpdatedBy = models.CharField(max_length=254, null=True)
	TaskType = models.CharField(max_length=254, null=True)

