from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=150)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=10)