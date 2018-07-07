from django import forms
from .models import UserTask
from django.db import models

class TaskForm(forms.ModelForm):

    class Meta:
        model = UserTask
        fields = ('task',)
