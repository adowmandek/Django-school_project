from django import forms
from django.db.models.base import Model
from django.forms import fields
from.models import Calender

class Calenderregistrationform(forms.ModelForm):
    class Meta:
        model=Calender
        fields="__all__"