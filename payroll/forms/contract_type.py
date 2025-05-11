
from django import forms
from payroll.models import  ContractType


class ContractTypeForm(forms.ModelForm):
    class Meta:
        model=ContractType
        fields='__all__'
        labels={
            'description':'Descripción',
        }
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }