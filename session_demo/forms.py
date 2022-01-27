from django import forms

# The model of the form that will be used to verify the integrity of the value submited
class OperationForm(forms.Form):
    value = forms.CharField(max_length=100)
    sign = forms.CharField(max_length=1)