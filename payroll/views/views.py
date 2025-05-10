from django.shortcuts import  redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def sign_up(request):
    try:
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('sign_in')
            return render(request,'sign_up.html',{'form':form,'error':'Error al crear el usuario'})
        else:  
            form=UserCreationForm()
            return render(request,'sign_up.html',{'form':form})
    except Exception:
        return render(request,'sign_up.html',{'form':form,'error':'Error al crear el usuario'})



def sign_in(request):
    try:
        if request.method=='POST':
            form=AuthenticationForm(request,request.POST)
            if form.is_valid():
                user=form.get_user()
                login(request,user)
                return redirect('payroll:home')
            return render(request,'sign_in.html',{'form':form,'error':'Error al Iniciar Sesión'})
        else:
            form=AuthenticationForm()
            return render(request,'sign_in.html',{'form':form})

    except Exception:
        return render(request,'sign_in.html',{'form':form,'error':'Error al Iniciar Sesión'})


def sign_out(request):
    logout(request)
    return redirect('sign_in')
      
@login_required(login_url='sign_in')
def home(request):
    return render(request,'home.html')



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