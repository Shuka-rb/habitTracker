from django import forms
from .models import Habit

class NameForm(forms.Form):
    class Meta:
        model = Habit
        fields = ["name", "description"]