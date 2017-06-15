# WIP - NOT YET OPERATIONAL
from django import forms


class AddItem(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
