from django.core.paginator import Paginator
import re

def paginator(request,objects):
    paginator=Paginator(objects,3)
    page_number=request.GET.get('page')
    registers=paginator.get_page(page_number)
    current_page = registers.number
    total_pages = paginator.num_pages

    pages_range = []
    for i in range(1, total_pages + 1):
        if abs(i - current_page) <= 2 or i == 1 or i == total_pages:
            pages_range.append(i)

    return {'registers': registers,'pages_range':pages_range,'current_page':current_page}
    

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
    