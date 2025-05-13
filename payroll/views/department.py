from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from payroll.forms.department import DepartmentForm
from payroll.models import Department
from payroll.helpers.utilies import paginator

@login_required(login_url='sign_in')
def list_department(request):
    try:
        query=request.GET.get('search',None)
        if query:
            departments=Department.objects.filter(description__icontains=query)
        else:
            departments=Department.objects.all()


        context=paginator(request,departments)
        return render(request,'department/list_departments.html',context)
    except Exception as e:
        print(f"Error: {e}")  
        return render(request,'department/list_departments.html',{'error':'Error al buscar'})

@login_required(login_url='sign_in')
def create_department(request):
    try:
        if request.method=='GET':
            form=DepartmentForm()
            return render(request,'department/create.html',{'form':form,'title':'Registrar Departamentos'})

        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_departments')
        return render(request,'department/create.html',{'form':form,'title':'Registrar Departamentos',
                                                     'error':'Formulario llenado incorrectamente'})
       
    except Exception as e:
        print(e)
        return render(request,'department/create.html',{'form':form,'title':'Registrar Departamentos',
                                                     'error':'Error al guardar el departamentos'})
    

@login_required(login_url='sign_in')
def update_department(request,id):
    try: 
        department=get_object_or_404(Department,id=id)
        if request.method=='GET':
            form=DepartmentForm(instance=department)
            return render(request,'department/create.html',{'form':form,'title':'Actualizar Departamentos'})

        form=DepartmentForm(request.POST,instance=department)
        if form.is_valid():
                form.save()
                return redirect('payroll:list_departments')
        return render(request,'department/create.html',{'form':form,'title':'Actualizar Departamentos','error':'Formulario llenado incorrectamente'})
        
    except:
        return render(request,'department/create.html',{'form':form,'title':'Actualizar Departamentos',
                                                     'error':'Error al actualizar departamentos'})



@login_required(login_url='sign_in')
def delete_department(request,id):
    try:
        department=get_object_or_404(Department,id=id)
        if request.method=='GET':
            return render(request,'department/delete.html',{'department':department,'title':'Eliminar Departamento'})

        department.delete()
        return redirect('payroll:list_departments')

        
    except Exception:
        return render(request,'department/delete.html',{'department':department,'error':'Error al eliminar departamento','title':'Eliminar Departamento'})
