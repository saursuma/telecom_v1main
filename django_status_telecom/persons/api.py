from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Persons

class PersonResource(ModelResource):
	class Meta:
		queryset = Persons.objects.all()
		resource_name = 'person'
		filtering = { "first_name" : ALL }
