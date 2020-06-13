from django import forms
from .models import Location

class GoogleForm(forms.ModelForm):
	map_url = forms.CharField()
	class Meta:
		model = Location
		fields = ["place", "map_url"]