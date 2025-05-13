from django.shortcuts import get_object_or_404, redirect, render
from payroll.forms.payslip import PayslipForm
from payroll.models import Payslip
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from payroll.helpers.utilies import paginator


@login_required(login_url='sign_in')
def list_payslip(request):
    try:
        query=request.GET.get('search',None)
        if query:
            list_payslips=Payslip.objects.filter(Q(employee__name__icontains=query)|Q(year_month__icontains=query)|Q(salary__icontains=query) | Q(overtime_hours__icontains=query) | Q(bonus__icontains=query)  |Q(iess__icontains=query) | Q(tot_ing__icontains=query) | Q(tot_des__icontains=query) | Q(neto__icontains=query))
        else:
            list_payslips=Payslip.objects.all()


        context=paginator(request,list_payslips)
        return render(request,'payslip/list_payslip.html',context)
    except Exception as e:
        print(f"Error: {e}")  
        return render(request,'payslip/list_payslip.html',{'error':'Error al buscar'})

@login_required(login_url='sign_in')
def create_payslip(request):
    try:
        if request.method=='GET':
            form=PayslipForm()
            return render(request,'payslip/create.html',{'form':form,'title':'Registrar rol'})

        form=PayslipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_payslip')
        return render(request,'payslip/create.html',{'form':form,'title':'Registrar rol','error':'Formulario llenado incorrectamente'})

    except Exception as e:
        print(e)
        return render(request,'payslip/create.html',{'form':form,'title':'Registrar rol','error':'Error al guardar el empleado'})
    

@login_required(login_url='sign_in')
def update_payslip(request,id):
    try: 
        payslip=get_object_or_404(Payslip,id=id)
        if request.method=='GET':
            form=PayslipForm(instance=payslip)
            return render(request,'payslip/create.html',{'form':form,'title':'Actualizar rol'})

        form=PayslipForm(request.POST,instance=payslip)
        if form.is_valid():
                form.save()
                return redirect('payroll:list_payslip')
        return render(request,'payslip/create.html',{'form':form,'title':'Actualizar rol','error':'Formulario llenado incorrectamente'})
        
    except:
        return render(request,'payslip/create.html',{'form':form,'title':'Actualizar rol','error':'Error al actualizar el empleado'})



@login_required(login_url='sign_in')
def delete_payslip(request,id):
    try:
        payslip=get_object_or_404(Payslip,id=id)
        if request.method=='GET':
            return render(request,'payslip/delete.html',{'payslip':payslip,'title':'Eliminar rol'})

        payslip.delete()
        return redirect('payroll:list_payslip')

        
    except Exception:
        return render(request,'payslip/delete.html',{'payslip':payslip,'error':'Error al eliminar el rol','title':'Eliminar rol'})
