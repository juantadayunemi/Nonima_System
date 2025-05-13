from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from payroll.forms.positions import PositionForm
from payroll.models import Position
from payroll.helpers.utilies import paginator
# Create your views here.


@login_required(login_url='sign_in')
def list_positions(request):
    query=request.GET.get('search',None)
    if query:
        list_positions=Position.objects.filter(description__icontains=query)
    else:
        list_positions=Position.objects.all()

    context=paginator(request,list_positions)

    return render(request,'position/list_positions.html',context)

@login_required(login_url='sign_in')
def create_position(request):
    try:
        if request.method=='GET':
            form=PositionForm()
            return render(request,'position/create.html',{'form':form,'title':'Registrar Cargo'})

        form=PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_positions')
        return render(request,'position/create.html',{'form':form,'title':'Registrar Cargo','error':'Formulario llenado incorrectamente'})
    
    except Exception:
        return render(request,'employee/create.html',{'form':form,'title':'Registrar Cargo','error':'Error al guardar el cargo'})
    

@login_required(login_url='sign_in')
def update_position(request,id):
    try:
        position=get_object_or_404(Position,id=id)
        if request.method=='GET':
            form=PositionForm(instance=position)
            return render(request,'position/create.html',{'form':form,'title':'Actualizar Cargo'})

        form=PositionForm(request.POST,instance=position)
        if form.is_valid():
            form.save()
            return redirect('payroll:list_positions')
        return render(request,'position/create.html',{'form':form,'title':'Actualizar Cargo','error':'Formulario llenado incorrectamente'})
    
    except Exception:
        return render(request,'position/create.html',{'form':form,'title':'Actualizar Cargo','error':'Error al guardar el cargo'})

@login_required(login_url='sign_in')
def delete_position(request,id):
    try:
        position=get_object_or_404(Position,id=id)
        if request.method=='GET':
            return render(request,'position/delete.html',{'position':position,'title':'Eliminar cargo'})

        position.delete()
        return redirect('payroll:list_positions')

        
    except Exception:
        return render(request,'position/delete.html',{'position':position,'error':'Error al eliminar el cargo','title':'Eliminar Cargo'})