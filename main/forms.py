from django import forms
from .models import Input

class InputForm(forms.ModelForm):
	comments = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Input
		fields = ["full_name","sex","age","contact_me","image","contact_number","email","comments"]
		widget = {"comments" : forms.Textarea(attrs={"cols" : "30", "rows" : "30"}),}


