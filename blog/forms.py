from django import forms
 
class PostForm(forms.Form):
    project_choices = (
    	('mobile', 'Mobile'),
    	('web', 'Web'),
    	('other', 'Other'),
    )
    project = forms.ChoiceField(choices=project_choices)
    status_choices = (
    	('new', 'New'),
    	('existing', 'Existing'),
    )
    status = forms.ChoiceField(choices=status_choices)
    timeline_choices = (
    	('now', 'Now'),
    	('week', 'One Week'),
    	('month', 'One Month'),
    	('months', 'Two Months'),
    )
    timeline = forms.ChoiceField(choices=timeline_choices)
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)