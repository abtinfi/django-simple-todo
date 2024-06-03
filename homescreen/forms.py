from django import forms
from .models import ToDo


class ToDoCreatForms(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateField()


class ToDoUpdateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'body', 'created')
