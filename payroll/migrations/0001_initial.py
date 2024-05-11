# Generated by Django 5.0.2 on 2024-05-11 03:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('announcement_id', models.AutoField(primary_key=True, serialize=False)),
                ('announcement_date', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('departmentId', models.AutoField(primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('benefit_id', models.AutoField(primary_key=True, serialize=False)),
                ('benefit_type', models.CharField(max_length=100)),
                ('benefit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('attendance_date', models.DateField()),
                ('check_in_time', models.DateTimeField()),
                ('check_out_time', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PayrollHistory',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('payroll_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_date', models.DateField()),
                ('gross_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_method', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalaryDetail',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('salary_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allowances', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deductions', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_period_start', models.DateField()),
                ('pay_period_end', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaxDetail',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('tax_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('tax_type', models.CharField(max_length=100)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('taxable_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField()),
                ('role', models.CharField(choices=[('Employee', 'Employee'), ('Admin', 'Admin')], max_length=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]