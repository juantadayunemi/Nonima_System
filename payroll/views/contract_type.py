from django.shortcuts import get_object_or_404, redirect, render
from payroll.forms.contract_type import ContractTypeForm
from payroll.models import ContractType
from django.contrib.auth.decorators import login_required
from payroll.helpers.utilies import paginator

@login_required(login_url='sign_in')
def list_contract_type(request):
    try:
        query=request.GET.get('search',None)
        if query:
            contract_types=ContractType.objects.filter(description__icontains=query)
        else:
            contract_types=ContractType.objects.all()


        context=paginator(request,contract_types)
        return render(request,'contract_type/list_contract_types.html',context)
    except Exception as e:
        print(f"Error: {e}")  
        return render(request,'contract_type/list_contract_types.html',{'error':'Error al buscar'})

@login_required(login_url='sign_in')
def create_contract_type(request):
    try:
        if request.method=='GET':
            form=ContractTypeForm()
            return render(request,'contract_type/create.html',{'form':form,'title':'Registrar Tipo de Contrato'})
    
        form=ContractTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_contract_types')
        return render(request,'contract_type/create.html',{'form':form,'title':'Registrar Tipo de Contrato',
                                                         'error':'Formulario llenado incorrectamente'})
    except Exception as e:
        print(e)
        return render(request,'contract_type/create.html',{'form':form,'title':'Registrar Tipo de Contrato',
                                                     'error':'Error al guardar el tipo de contrato'})
    

@login_required(login_url='sign_in')
def update_contract_type(request,id):
    try: 
        contract_type=get_object_or_404(ContractType,id=id)
        if request.method=='GET':
            form=ContractTypeForm(instance=contract_type)
            return render(request,'contract_type/create.html',{'form':form,'title':'Actualizar tipo de contrato'})

        form=ContractTypeForm(request.POST,instance=contract_type)
        if form.is_valid():
                form.save()
                return redirect('payroll:list_contract_types')
        return render(request,'contract_type/create.html',{'form':form,'title':'Actualizar tipo de contrato','error':'Formulario llenado incorrectamente'})
        
    except:
        return render(request,'contract_type/create.html',{'form':form,'title':'Actualizar tipo de contrato',
                                                     'error':'Error al actualizar el empleado'})


@login_required(login_url='sign_in')
def delete_contract_type(request,id):
    try:
        contract_type=get_object_or_404(ContractType,id=id)
        if request.method=='GET':
            return render(request,'contract_type/delete.html',{'contract_type':contract_type,'title':'Eliminar Tipo de Contrato'})

        contract_type.delete()
        return redirect('payroll:list_contract_types')
        
    except Exception:
        return render(request,'contract_type/delete.html',{'contract_type':contract_type,'error':'Error al eliminar el Tipo de contrato','title':'Eliminar Tipo de Contrato'})
