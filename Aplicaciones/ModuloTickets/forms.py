from dataclasses import field
from django import forms
from .models import tickets

class ticketsForm(forms.ModelForm):
   class Meta:
       model = tickets
       fields = '__all__'