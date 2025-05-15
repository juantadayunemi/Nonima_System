from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from payroll.forms.employees import EmployeeForm
from payroll.forms.permiso import PermisoForm
from payroll.models import Employee, Permiso, TipoPermiso
from django.db.models import Q
from payroll.helpers.utilies import is_valid_dni, paginator
# Create your views here.


@login_required(login_url='sign_in')
def list_permiso(request):
    try:
        query = request.GET.get('search', None)
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        tipo_permiso = request.GET.get('tipo_permiso')
        is_active = request.GET.get('status_filter')  # puede ser 'active' o 'inactive'

        list_permisos = Permiso.objects.all()

        if query:
            list_permisos = list_permisos.filter(
                Q(employee__name__icontains=query) |
                Q(employee__dni__icontains=query) 
            )

        if start_date:
            list_permisos = list_permisos.filter(fecha_permiso__gte=start_date)

        if end_date:
            list_permisos = list_permisos.filter(fecha_permiso__lte=end_date)

        if tipo_permiso:
            list_permisos = list_permisos.filter(tipo_permiso_id=tipo_permiso)

        if is_active == 'active':
            list_permisos = list_permisos.filter(is_active=True)
        elif is_active == 'inactive':
            list_permisos = list_permisos.filter(is_active=False)

        context = paginator(request, list_permisos)
        context['tipo_permisos'] = TipoPermiso.objects.all()

        return render(request, 'permiso/list_permisos.html', context)

    except Exception as e:
        context = {'error': 'Error al buscar'}
        return render(request, 'permiso/list_permisos.html', context)

@login_required(login_url='sign_in')
def create_permiso(request):
    try:   
        if request.method=='GET':
            form=PermisoForm()
            return render(request,'permiso/create.html',{'form':form,'title':'Registrar Permiso'})

        form=PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_permisos')
        return render(request,'permiso/create.html',{'form':form,'title':'Registrar Permiso','error':'Formulario llenado incorrectamente'})

    except Exception as ex:
        return render(request,'permiso/create.html',{'form':form,'title':'Registrar Permiso','error':'Error al guardar el permiso' + str(ex)})


@login_required(login_url='sign_in')
def update_permiso(request,id):
    try:
        permiso=get_object_or_404(Permiso,id=id)
        if request.method=='GET':
            form=PermisoForm(instance=permiso)
            return render(request,'permiso/create.html',{'form':form,'title':'Actualizar Permiso'})


        form=PermisoForm(request.POST,instance=permiso)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_permisos')
        return render(request,'permiso/create.html',{'form':form,'title':'Actualizar Permiso','error':'Formulario llenado incorrectamente'})

    except Exception:
        return render(request,'permiso/create.html',{'form':form,'title':'Actualizar Permiso','error':'Error al guardar el permiso'})

@login_required(login_url='sign_in')
def delete_permiso(request,id):
    try:
        permiso=get_object_or_404(Permiso,id=id)
        if request.method=='GET':
            return render(request,'permiso/delete.html',{'permiso':permiso,'title':'Eliminar permiso'})

        permiso.delete()
        return redirect('payroll:list_permisos')

    except Exception:
        return render(request,'permiso/delete.html',{'permiso':permiso,'error':'Error al eliminar el permiso','title':'Eliminar permiso'})


def get_tipopermiso_data(request, permiso_id):
    try:
        permiso = TipoPermiso.objects.get(pk=permiso_id)
        return JsonResponse({
            'frecuencia_dias': permiso.frecuencia_dias,
            'description': permiso.descripcion,
        })
    except TipoPermiso.DoesNotExist:
        return JsonResponse({'error': 'Tipo de permiso no encontrado'}, status=404)