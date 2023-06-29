from django import forms


class ActivityForm(forms.Form):
    activity_name = forms.CharField(label="Name of the activity", max_length=100)
    start_date=forms.DateField()
    end_date=forms.DateField()
    file=forms.FileField(label="Upload your certificate")

