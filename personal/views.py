from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .models import  *
from .forms import PersonaForm
# Create your views here.
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

# Funcion para crear persona
def persona_list(request):
    personal = Persona.objects.all()
    context = {
        'personal': personal,
    }
    return render(request, 'personal/persona_list.html', context)

# Carga formulario para crear empleado
def persona_create(request):
    form = PersonaForm
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        form.save()
        return redirect('personal:persona_list')
    return render(request, 'personal/persona_create.html', context)


# Ver detalle del empleado
def persona_detail(request, pk):
    persona = Persona.objects.get(pk = pk)
    context = {
        'persona': persona,
    }
    return render(request, 'personal/persona_detail.html', context)

# Editar empleado
def persona_edit(request, pk):
    persona = Persona.objects.get(pk = pk)
    form = PersonaForm(instance=persona)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        form.save()
        return redirect('personal:persona_list')
    return render(request, 'personal/persona_create.html', context)

# Eliminar empleado
def persona_delete(request, pk):
    persona = Persona.objects.get(pk = pk)
    context = {
        'persona': persona,
    }
    if request.method == 'POST':
        persona.delete()
        return redirect('personal:persona_list')
    return render(request, 'personal/persona_delete.html', context)