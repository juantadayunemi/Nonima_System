
from django import forms
from payroll.models import  Position


class PositionForm(forms.ModelForm):
    class Meta:
        model=Position
        fields='__all__'
        labels={
            'description':'descripción',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }