# payroll/forms/asistencia.py
from django import forms

from payroll.models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['employee', 'fecha', 'hora_entrada', 'hora_salida', 'estado', 'observaciones', 'is_active']
        
        widgets = {
            'fecha': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'DD/MM/YYYY'
            }),
            'hora_entrada': forms.TimeInput(attrs={
                'class': 'form-control timepicker',
                'placeholder': 'HH:MM'
            }),
            'hora_salida': forms.TimeInput(attrs={
                'class': 'form-control timepicker',
                'placeholder': 'HH:MM'
            }),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_entrada = cleaned_data.get('hora_entrada')
        hora_salida = cleaned_data.get('hora_salida')
        
        if hora_entrada and hora_salida:
            if hora_salida <= hora_entrada:
                self.add_error('hora_salida', 'La hora de salida debe ser posterior a la hora de entrada')
        
        return cleaned_data