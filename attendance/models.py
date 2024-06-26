from django.db import models
from django.utils import timezone
from employee.models import Employee
import xlsxwriter

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class Attendance(BaseModel):
    attendance_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_log = models.DateField()
    am_in = models.TimeField(null=True)
    remarks = models.CharField(max_length=255, null=True)
    am_in_mask = models.CharField(max_length=255, null=True)
    am_out = models.TimeField(null=True)
    am_out_mask = models.CharField(max_length=255, null=True)
    pm_in = models.TimeField(null=True)
    pm_in_mask = models.CharField(max_length=255, null=True)
    pm_out = models.TimeField(null=True)
    pm_out_mask = models.CharField(max_length=255, null=True)

    objects = models.Manager()