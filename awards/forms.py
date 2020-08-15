from django import forms

class AwardsForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=30)
    email = forms.EmailField(label='Email')