from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import *

# Create your views here.
# Ingresos
def ingreso_form(request):
    ingreso_form = IngresoForm()
    context = {
        'transaccion_form': ingreso_form,
        'title': "Ingreso",
    }
    return render(request, 'transacciones/transaccion_form.html', context)


class IngresoCreateView(CreateView):
    model = Transaccion
    form_class = IngresoForm
    # template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy('transacciones:ingreso_list')

    def form_valid(self, form):
        transaccion = form.save()
        transaccion.tipo = 'i'
        transaccion.save()
        return super(IngresoCreateView, self).form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super(IngresoCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Ingreso'})
        return context

def ingreso_list(request):
    ingresos = Transaccion.objects.filter(tipo = 'i')
    context = {
        'transacciones': ingresos,
        'title': 'Ingreso',
        'form_create': 'transacciones:ingreso_form',
    }
    return render(request, 'transacciones/transacciones_list.html', context)    


class GastoCreateView(CreateView):
    model = Transaccion
    form_class = GastoForm
    # template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy('transacciones:gasto_list')

    def form_valid(self, form):
        transaccion = form.save()
        transaccion.tipo = 'g'
        transaccion.save()
        return super(GastoCreateView, self).form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super(GastoCreateView, self).get_context_data(**kwargs)
        context.update({'title': 'Gasto'})
        return context


def gasto_list(request):
    gastos = Transaccion.objects.filter(tipo = 'g')
    context = {
        'transacciones': gastos,
        'title': 'Gasto',
        'form_create': 'transacciones:gasto_form',
    }
    return render(request, 'transacciones/transacciones_list.html', context)