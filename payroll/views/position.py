from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from payroll.forms.positions import PositionForm
from payroll.models import Position
from payroll.helpers.utilies import paginator
# Create your views here.


# @login_required(login_url='sign_in')
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
        if request.method=='POST':
            form=PositionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('payroll:list_positions')
            return render(request,'position/create.html',{'form':form,'title':'Registrar posición','error':'Formulario llenado incorrectamente'})
        form=PositionForm()
        return render(request,'position/create.html',{'form':form,'title':'Registrar posición'})
    except Exception:
        return render(request,'employee/create.html',{'form':form,'title':'Registrar empleado','error':'Error al guardar el empleado'})
    

@login_required(login_url='sign_in')
def update_position(request,id):
    try:
        position=get_object_or_404(Position,id=id)
        if request.method=='POST':
            form=PositionForm(request.POST,instance=position)
            if form.is_valid():
                form.save()
                return redirect('payroll:list_positions')
            return render(request,'position/create.html',{'form':form,'title':'Actualizar posición','error':'Formulario llenado incorrectamente'})

        form=PositionForm(instance=position)
        return render(request,'position/create.html',{'form':form,'title':'Actualizar posición'})
    except Exception:
        return render(request,'position/create.html',{'form':form,'title':'Actualizar posición','error':'Error al guardar la posición'})

@login_required(login_url='sign_in')
def delete_position(request,id):
    try:
        position=get_object_or_404(Position,id=id)
        if request.method=='POST':
            position.delete()
            return redirect('payroll:list_positions')

        return render(request,'position/delete.html',{'position':position,'title':'Eliminar cargo'})
    except Exception:
        return render(request,'position/delete.html',{'position':position,'error':'Error al eliminar la cargo','title':'Actualizar posición'})