from dataclasses import field
from django import forms
from .models import Usuario

class usuarioForm(forms.ModelForm):
   class Meta:
       model = Usuario
       fields = '__all__'