import datetime
from haystack import indexes
from persons.models import Persons
import logging

logr = logging.getLogger(__name__)



class PersonIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.NgramField(document=True, use_template=True)
	#pub_date = indexes.DateTimeField(model_attr='pub_date')
	#logr.debug(str(text))
	
	content_auto = indexes.NgramField(model_attr='first_name')
	logr.debug(content_auto)

	def get_model(self):
		return Persons
	
	def index_queryset(self, using=None):
		return self.get_model().objects.all()
	
