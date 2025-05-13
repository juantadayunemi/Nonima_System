from django.shortcuts import  redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required




# Create your views here.


def sign_up(request):
    try:
        if request.method=='GET':
            form=UserCreationForm()
            return render(request,'sign_up.html',{'form':form})
        else:  
            form=UserCreationForm(request.POST)
            if form.is_valid():
                user=form.save()
                login(request,user)
                return redirect('payroll:dashboard')
            return render(request,'sign_up.html',{'form':form,'error':'Error al crear el usuario'})
    except Exception:
        return render(request,'sign_up.html',{'form':form,'error':'Error al crear el usuario'})



def sign_in(request):
    try:
        if request.method=='GET':
            form=AuthenticationForm()
            return render(request,'sign_in.html',{'form':form})     
        else:
            form=AuthenticationForm(request,request.POST)
            # if form.is_valid():
            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user is None:
                return render(request,'sign_in.html',{'form':form,'error':'El usuario o contraseña es incorrecta'})
            login(request,user)
            return redirect('payroll:dashboard')
            # return render(request,'sign_in.html',{'form':form,'error':'Error al Iniciar Sesión'})

    except Exception:
        return render(request,'sign_in.html',{'form':form,'error':'Error al Iniciar Sesión'})


def sign_out(request):
    logout(request)
    return redirect('sign_in')
      

def home(request):
    if request.user.is_authenticated:
        return redirect('payroll:dashboard')
    return render(request,'home.html')

@login_required(login_url='sign_in')
def dashboard(request):
    return render(request,'dashboard.html')



