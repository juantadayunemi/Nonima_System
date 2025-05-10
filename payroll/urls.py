from django.urls import path
from payroll.views import auth,employees,payslip,position


app_name='payroll'
urlpatterns = [ path('',auth.home,name='home'),
    path('sign/out/',auth.sign_out,name='sign_out'),
    path('list/employees/',employees.list_employee,name='list_employees'),
    path('create/employee/',employees.create_employee,name='create_employee'),
    path('update/employee/<int:id>/',employees.update_employee,name='update_employee'),
    path('delete/employee/<int:id>/',employees.delete_employee,name='delete_employee'),
    path('create_position/',position.create_position,name='create_position'),
    path('list_positions/',position.list_positions,name='list_positions'),
    path('update_position/<int:id>/',position.update_position,name='update_position'),
    path('delete_position/<int:id>/',position.delete_position,name='delete_position'),
     path('list/payslips/', payslip.list_payslip, name='list_payslip'),
    path('create/payslip/', payslip.create_payslip, name='create_payslip'),
    path('update/payslip/<int:id>/', payslip.update_payslip, name='update_payslip'),
    path('delete/payslip/<int:id>', payslip.delete_payslip, name='delete_payslip'),
   
]