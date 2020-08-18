from django import forms
from .models import Submission, Votes

class AwardsForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=30)
    email = forms.EmailField(label='Email')

class NewSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        exclude = ['developer', 'submission_date']
        widget = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewVoteForm(forms.ModelForm):

    class Meta:
        model = Votes
        exclude = ['developer', 'submission']
        widget = {
            'design': forms.IntegerField(label='Enter a value between 1 - 10', min_value=0, max_value=10),
            'usability': forms.IntegerField(min_value=0, max_value=10),
            'content': forms.IntegerField(min_value=0, max_value=10),
        }