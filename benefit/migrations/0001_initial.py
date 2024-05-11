# Generated by Django 5.0.2 on 2024-05-11 15:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('benefit_id', models.AutoField(primary_key=True, serialize=False)),
                ('benefit_type', models.CharField(max_length=100)),
                ('benefit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('benefit_description', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]