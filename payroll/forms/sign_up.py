from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': ''
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })

def is_valid_dni(cedula):
    """
    Valida una cédula ecuatoriana
    Formatos válidos: 0102030405 o 01-020-304-05
    """
    # Limpiar guiones y espacios
    cedula = re.sub(r'[-\s]', '', cedula)
    
    # Validar longitud (10 dígitos)
    if len(cedula) != 10 or not cedula.isdigit():
        return False
    
    # Validar provincia (primeros dos dígitos entre 01 y 24)
    provincia = int(cedula[:2])
    if provincia < 1 or provincia > 24:
        return False
    
    # Algoritmo de validación (módulo 10)
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    verificador = int(cedula[-1])
    suma = 0
    
    for i in range(9):
        valor = int(cedula[i]) * coeficientes[i]
        suma += valor if valor < 10 else valor - 9
    
    digito_verificador = (10 - (suma % 10)) % 10
    
    return digito_verificador == verificador        