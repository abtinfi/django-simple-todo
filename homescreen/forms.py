from django import forms

class ToDoCreatForms(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateField()
