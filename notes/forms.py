from django import forms
from .models import ToDoList_data

WHEN = (
	('today','Today'),
	('tomorrow', 'Tomorrow'),
	('thisWeek', 'This week'),
	('nextWeek', 'Next week'),
	('future', 'Future'),
)

class ToDoList_form(forms.ModelForm):
	title = forms.CharField(label = 'Title')
	text = forms.CharField(label = "Note")
	when = forms.ChoiceField(choices = WHEN)
	class Meta:
		model = ToDoList_data
		fields = ["when", "title", "text"]