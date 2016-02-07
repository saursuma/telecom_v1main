from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		
		if commit:
			user.save()
		return user
class ContactForm1(forms.Form):
	subject = forms.CharField(max_length=100)
class ContactForm2(forms.Form):
	sender = forms.EmailField()
class ContactForm3(forms.Form):
	message = forms.CharField(widget=forms.Textarea)


