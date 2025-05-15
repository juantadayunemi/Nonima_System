from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from payroll.forms.asistencia import AsistenciaForm
from payroll.models import Asistencia
from django.db.models import Q
from payroll.helpers.utilies import is_valid_dni, paginator


# payroll/views.py
@login_required(login_url='sign_in')
def list_asistencia(request):
    try:
        asistencias = Asistencia.objects.all()
        # Filtros similares al de permisos
        context = paginator(request, asistencias)
        return render(request, 'asistencia/list_asistencia.html', context)
    except Exception as e:
        return render(request, 'asistencia/list_asistencia.html', {'error': str(e)})

@login_required(login_url='sign_in')
def create_asistencia(request):
    try:
        if request.method == 'POST':
            form = AsistenciaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('payroll:list_asistencia')
            return render(request, 'asistencia/create.html', {'form': form, 'error': 'Datos inválidos'})
        return render(request, 'asistencia/create.html', {'form': AsistenciaForm()})
    except Exception as e:
        return render(request, 'asistencia/create.html', {'error': str(e)})

# Implementar similarmente update_asistencia y delete_asistencia
@login_required(login_url='sign_in')
def update_asistencia(request, id):
    try:
        asistencia = Asistencia.objects.get(pk=id)
        if request.method == 'POST':
            form = AsistenciaForm(request.POST, instance=asistencia)
            if form.is_valid():
                form.save()
                return redirect('payroll:list_asistencia')
            return render(request, 'asistencia/create.html', {'form': form, 'error': 'Datos inválidos'})
        return render(request, 'asistencia/create.html', {'form': AsistenciaForm(instance=asistencia)})
    except Exception as e:
        return render(request, 'asistencia/create.html', {'error': str(e)})

@login_required(login_url='sign_in')
def delete_asistencia(request, id):
    try:
        asistencia = Asistencia.objects.get(id=id)
        asistencia.delete()
        return redirect('payroll:list_asistencia')
    except Exception as e:
        return render(request, 'asistencia/list.html', {'error': str(e)})