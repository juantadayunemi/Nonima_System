from django.urls import path

from payroll.views import views,employees


app_name='payroll'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('sign/out/',views.sign_out,name='sign_out'),
    path('list/employees/',employees.list_employee,name='list_employees'),
    path('create/employee/',employees.create_employee,name='create_employee'),
    path('update/employee/<int:id>/',employees.update_employee,name='update_employee'),
    path('delete/employee/<int:id>',employees.delete_employee,name='delete_employee'),
]