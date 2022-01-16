from django import forms

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=100)
    price = forms.IntegerField()
    stock = forms.IntegerField()