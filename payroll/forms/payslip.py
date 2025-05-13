from django import forms

from payroll.models import Payslip

class PayslipForm(forms.ModelForm):
    class Meta:
        model=Payslip
        fields=['employee','year_month','salary','overtime_hours','bonus']
        labels={
            'employee':'Empleado',
            'year_month':'Año-Mes',
            'salary':'Salario',
            'overtime_hours':'Horas extras',
            'bonus':'Bono'
        }
        widgets = {
            'employee': forms.Select(attrs={'class':'form-control'}),
            'year_month': forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control','type': 'date'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'overtime_hours':forms.NumberInput(attrs={'class':'form-control'}),
            'bonus':forms.NumberInput(attrs={'class':'form-control'})
        }