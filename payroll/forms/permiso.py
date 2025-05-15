from django import forms
from django.core.exceptions import ValidationError
from payroll.models import Permiso

class PermisoForm(forms.ModelForm):

    class Meta:
        model = Permiso
        fields = ['employee', 'fecha_permiso', 'tipo_permiso', 'dias','horas','is_active']
        labels = {
            'employee': 'Empleado',
            'fecha_permiso': 'Fecha de Permiso',
            'tipo_permiso': 'Tipo de Permiso',
            'dias': 'Días',
            'horas': 'Horas',
            'is_active': 'Activo'
        }
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'fecha_permiso': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'id': 'fecha_permiso',
                'autocomplete': 'off',
                'placeholder': 'DD/MM/YYYY',
            }),
            'tipo_permiso': forms.Select(attrs={'class': 'form-control'}),
            'dias': forms.NumberInput(attrs={'class': 'form-control', 'step': 1, 'min': 0}),
            'horas': forms.NumberInput(attrs={'class': 'form-control', 'step': 1, 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean(self):
        cleaned_data = super().clean()
        tipo_permiso = cleaned_data.get('tipo_permiso')
        dias = cleaned_data.get('dias')
        horas = cleaned_data.get('horas')

        if tipo_permiso:
            if tipo_permiso.frecuencia_dias:  # Si es permiso por días
                if dias is None or dias <= 0:
                    self.add_error('dias', 'Debe ingresar al menos 1 día.')
                cleaned_data['horas'] = None  # Forzar a null
            else:  # Si es permiso por horas
                if horas is None or horas <= 0:
                    self.add_error('horas', 'Debe ingresar al menos 1 hora.')
                cleaned_data['dias'] = None  # Forzar a null

        return cleaned_data
