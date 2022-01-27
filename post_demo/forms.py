from django import forms

# The model of the form that will be used to verify the integrity of the value submited
class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=100)
    price = forms.IntegerField()
    stock = forms.IntegerField()