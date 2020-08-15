from django import forms
from .models import Submission

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