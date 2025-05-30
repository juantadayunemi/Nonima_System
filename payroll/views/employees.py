from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from payroll.forms.employees import EmployeeForm
from payroll.models import Employee
from django.db.models import Q
from payroll.helpers.utilies import is_valid_dni, paginator
# Create your views here.


@login_required(login_url='sign_in')
def list_employee(request):
    try:
        query=request.GET.get('search',None)
        if query: 
            list_employees=Employee.objects.filter(Q(name__icontains=query) | Q(dni__icontains=query) | Q(address__icontains=query) | Q(sex__icontains=query) | Q(salary__icontains=query) | Q(position__description__icontains=query) | Q(department__description__icontains=query) |Q(contract_type__description__icontains=query))
        else: 
            list_employees=Employee.objects.all()

        context=paginator(request,list_employees)

        return render(request,'employee/list_employees.html',context)
    except Exception:
        context['error']='Error al buscar'
        return render(request,'employee/list_employees.html',context)

@login_required(login_url='sign_in')
def create_employee(request):
    try:   
        if request.method=='GET':
            form=EmployeeForm()
            return render(request,'employee/create.html',{'form':form,'title':'Registrar Empleado'})

        form=EmployeeForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data.get('dni') 
            if not is_valid_dni(dni):
                return render(request, 'employee/create.html', {
                            'form': form,
                            'title': 'Registrar empleado',
                            'error': 'Cédula ecuatoriana inválida'
                        })
            form.save()
            return redirect('payroll:list_employees')
        return render(request,'employee/create.html',{'form':form,'title':'Registrar Empleado','error':'Formulario llenado incorrectamente'})
        
    except Exception:
        return render(request,'employee/create.html',{'form':form,'title':'Registrar Empleado','error':'Error al guardar el empleado'})
    

@login_required(login_url='sign_in')
def update_employee(request,id):
    try:
        employee=get_object_or_404(Employee,id=id)
        if request.method=='GET':
            form=EmployeeForm(instance=employee)
            return render(request,'employee/create.html',{'form':form,'title':'Actualizar Empleado'})


        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            dni = form.cleaned_data.get('dni') 
            if not is_valid_dni(dni):
                return render(request, 'employee/create.html', {
                            'form': form,
                            'title': 'Registrar empleado',
                            'error': 'Cédula ecuatoriana inválida'
                        })
            form.save()
            return redirect('payroll:list_employees')
        return render(request,'employee/create.html',{'form':form,'title':'Actualizar Empleado','error':'Formulario llenado incorrectamente'})
    
        
    except Exception:
        return render(request,'employee/create.html',{'form':form,'title':'Actualizar Empleado','error':'Error al guardar el empleado'})
    

@login_required(login_url='sign_in')
def delete_employee(request,id):
    try:
        employee=get_object_or_404(Employee,id=id)
        if request.method=='GET':
            return render(request,'employee/delete.html',{'employee':employee,'title':'Eliminar empleado'})

        employee.delete()
        return redirect('payroll:list_employees')

    except Exception:
        return render(request,'employee/delete.html',{'employee':employee,'error':'Error al eliminar el empleado','title':'Eliminar empleado'})
    


def get_employee_data(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        return JsonResponse({
            'salary': str(employee.salary),
            'name': employee.name,
        })
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)