from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render

from personas.models import Persona
from personas.forms import PersonaForm

# Create your views here.
# PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})