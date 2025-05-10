from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from payroll.forms.positions import PositionForm
from payroll.models import Position
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


# @login_required(login_url='sign_in')
def list_positions(request):
    query=request.GET.get('search',None)
    if query:
        list_positions=Position.objects.filter(Q(description__icontains=query))
    else:
        list_positions=Position.objects.all()

    context=paginator(request,list_positions)

    return render(request,'position/list_positions.html',context)

# @login_required(login_url='sign_in')
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
    

# @login_required(login_url='sign_in')
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

# @login_required(login_url='sign_in')
def delete_position(request,id):
    try:
        position=get_object_or_404(Position,id=id)
        if request.method=='POST':
            position.delete()
            return redirect('payroll:list_positions')

        return render(request,'position/delete.html',{'position':position,'title':'Eliminar cargo'})
    except Exception:
        return render(request,'position/delete.html',{'position':position,'error':'Error al eliminar la cargo','title':'Actualizar posición'})