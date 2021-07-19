from django import forms
from django.forms import widgets
from .models import *
import datetime

class DateInput(forms.DateInput):
	input_type = 'date'
	initial = datetime.date.today()

class PersonaForm(forms.ModelForm):
    """Form definition for Persona."""

    class Meta:
        """Meta definition for Personaform."""

        model = Persona
        fields = '__all__'
        widgets =  {
            'fecha_nacimiento': DateInput(),
        }
