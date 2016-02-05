from django import forms
from models import Persons
from models import Comment
from models import Site
from models import Task

class PersonForm(forms.ModelForm):
	
	class Meta:
		model = Persons
		fields = ('first_name' , 'last_name','address', 'role', 'thumbnail')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('person', 'task', 'description', 'TaskType')


class SiteForm(forms.ModelForm):

	class Meta:
		model = Site
		fields = ('site_id', 'name','latitude','longitude','description')
        
class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('person', 'site','description','task_status','task_priority','task_type')
