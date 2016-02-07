from django import forms
from models import UserProfile

class UserProfilesForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('like_cheese','favourite_hamster_name')

