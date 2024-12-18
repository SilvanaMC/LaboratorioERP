from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import Laboratorio
from .forms import LaboratorioForm

def lista_laboratorios(request):
    laboratorio = Laboratorio.objects.all()
    return render(request, 'laboratorio/lista_laboratorios.html', {'laboratorio': laboratorio })

def detalle_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    return render(request, 'laboratorio/detalle_laboratorio.html', {'laboratorio': laboratorio})

def nuevo_laboratorio(request):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            laboratorio = form.save()
            return redirect('laboratorio:detalle_laboratorio', id=laboratorio.id)
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/nuevo_laboratorio.html', {'form': form})

def editar_laboratorio(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            laboratorio = form.save()
            return redirect('laboratorio:detalle_laboratorio', id=laboratorio.id)
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/editar_laboratorio.html', {'form': form})

def eliminar_laboratorio(request, id):
    laboratorio = Laboratorio.objects.filter(id=id).first()
    if not laboratorio:
        return HttpResponseNotFound("No se encontró el laboratorio especificado")

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio:lista_laboratorios')

    return render(request, 'laboratorio/eliminar_laboratorio.html', {'laboratorio': laboratorio})
