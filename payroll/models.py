from django.db import models

# Create your models here.
class Position(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Department(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description



class ContractType(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description



class Employee(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ]
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    contract_type = models.ForeignKey(ContractType,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year_month = models.DateField()#202501
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_hours = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    iess = models.DecimalField(max_digits=10, decimal_places=2)
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2)
    neto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee