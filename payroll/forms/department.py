
from django import forms
from payroll.models import  Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        labels={
            'description':'Descripción',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }