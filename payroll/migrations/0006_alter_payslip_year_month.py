# Generated by Django 5.2.1 on 2025-05-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_alter_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='year_month',
            field=models.IntegerField(),
        ),
    ]
