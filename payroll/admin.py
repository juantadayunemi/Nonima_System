from django.contrib import admin

from payroll.models import ContractType, Department, Employee, Payslip, Position, TipoPermiso

# Register your models here.
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(ContractType)
admin.site.register(Employee)
admin.site.register(Payslip)
admin.site.register(TipoPermiso)
