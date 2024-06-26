# Generated by Django 5.0.2 on 2024-05-11 14:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
    ]
