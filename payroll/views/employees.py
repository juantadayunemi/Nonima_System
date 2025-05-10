from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from payroll.forms.employees import EmployeeForm
from payroll.models import Employee
from django.db.models import Q
# Create your views here.


def paginator(request,objects):
    paginator=Paginator(objects,3)
    page_number=request.GET.get('page')
    registers=paginator.get_page(page_number)
    current_page = registers.number
    total_pages = paginator.num_pages

    pages_range = []
    for i in range(1, total_pages + 1):
        if abs(i - current_page) <= 2 or i == 1 or i == total_pages:
            pages_range.append(i)

    return {'registers': registers,'pages_range':pages_range,'current_page':current_page}


@login_required(login_url='sign_in')
def list_employee(request):
    query=request.GET.get('search',None)
    if query: 
        list_employees=Employee.objects.filter(Q(name__icontains=query) | Q(dni__icontains=query) | Q(address__icontains=query) | Q(sex__icontains=query) | Q(salary__icontains=query))
    else: 
        list_employees=Employee.objects.all()

    context=paginator(request,list_employees)

    return render(request,'employee/list_employees.html',context)

@login_required(login_url='sign_in')
def create_employee(request):
    try:
        if request.method=='POST':
            form=EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('payroll:list_employees')
            return render(request,'employee/create.html',{'form':form,'title':'Registrar empleado','error':'Formulario llenado incorrectamente'})
        form=EmployeeForm()
        return render(request,'employee/create.html',{'form':form,'title':'Registrar empleado'})
    except Exception:
        return render(request,'employee/create.html',{'form':form,'title':'Registrar empleado','error':'Error al guardar el empleado'})
    

@login_required(login_url='sign_in')
def update_employee(request,id):
    try:
        employee=get_object_or_404(Employee,id=id)
        if request.method=='POST':
            form=EmployeeForm(request.POST,instance=employee)
            if form.is_valid():
                form.save()
                return redirect('payroll:list_employees')
            return render(request,'employee/create.html',{'form':form,'title':'Actualizar empleado','error':'Formulario llenado incorrectamente'})
        
        form=EmployeeForm(instance=employee)
        return render(request,'employee/create.html',{'form':form,'title':'Actualizar empleado'})
    except Exception:
        return render(request,'employee/create.html',{'form':form,'title':'Actualizar empleado','error':'Error al guardar el empleado'})
    

@login_required(login_url='sign_in')
def delete_employee(request,id):
    try:
        employee=get_object_or_404(Employee,id=id)
        if request.method=='POST':
            employee.delete()
            return redirect('payroll:list_employees')

        return render(request,'employee/delete.html',{'employee':employee,'title':'Actualizar empleado'})
    except Exception:
        return render(request,'employee/delete.html',{'employee':employee,'error':'Error al eliminar el empleado','title':'Actualizar empleado'})