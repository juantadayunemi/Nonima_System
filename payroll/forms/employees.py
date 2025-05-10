

from django import forms
from payroll.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        labels={
            'name':'Nombre',
            'dni':'Cédula',
            'address':'Dirección',
            'sex':'sexo',
            'salary':'Salario',
            'position':'Cargo',
            'department':'Departamento',
            'contract_type':'Tipo de contrato'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'contract_type': forms.Select(attrs={'class': 'form-control'})
        }