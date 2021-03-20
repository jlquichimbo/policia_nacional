from django import forms
from .models import *
import datetime

class DateInput(forms.DateInput):
	input_type = 'date'
	initial = datetime.date.today()

class IngresoForm(forms.ModelForm):
    """IngresoForm definition."""
    class Meta:
        model = Transaccion
        fields = "__all__"
        exclude = ('tipo',)
        widgets = {
			'fecha': DateInput(),
        }
