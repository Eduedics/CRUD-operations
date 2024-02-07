from .models import Tasks
from django import forms
from django.forms import ModelForm

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['Name','Description','Status']
        