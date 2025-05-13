from django import forms
from payroll.models import Payslip

class PayslipForm(forms.ModelForm):
    year = forms.IntegerField(min_value=2000, max_value=2100, label='Año')
    month = forms.ChoiceField(
        choices=[
            (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'),
            (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'),
            (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'),
            (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
        ],
        label='Mes'
    )

    class Meta:
            model = Payslip
            fields = ['employee', 'salary', 'overtime_hours', 'bonus']
            labels = {
                'employee': 'Empleado',
                'salary': 'Salario',
                'overtime_hours': 'Horas Extras',
                'bonus': 'Bono',
            }
            widgets = {
                'employee': forms.Select(attrs={'class': 'form-control'}),
                'salary': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
                'overtime_hours': forms.NumberInput(attrs={'class': 'form-control'}),
                'bonus': forms.NumberInput(attrs={'class': 'form-control'})
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si es edición, extraer año y mes del valor actual de year_month
        if self.instance and self.instance.year_month:
            year = self.instance.year_month // 100
            month = self.instance.year_month % 100
            self.fields['year'].initial = year
            self.fields['month'].initial = month

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Combinar año y mes en formato YYYYMM
        year = self.cleaned_data['year']
        month = int(self.cleaned_data['month'])
        instance.year_month = year * 100 + month

        if commit:
            instance.save()
        return instance