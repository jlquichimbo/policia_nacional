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

    
    def __init__(self, *args, **kwargs):
        super(IngresoForm, self).__init__(*args, **kwargs)
        categorias_ingresos = Categoria.objects.filter(tipo ='i')
        self.fields['categoria'].queryset = categorias_ingresos


class GastoForm(forms.ModelForm):
    """GastoForm definition."""
    class Meta:
        model = Transaccion
        fields = "__all__"
        exclude = ('tipo',)
        widgets = {
			'fecha': DateInput(),
        }

    
    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)
        categorias_ingresos = Categoria.objects.filter(tipo ='g')
        self.fields['categoria'].queryset = categorias_ingresos