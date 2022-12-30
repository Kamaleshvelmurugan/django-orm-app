from django.db import models
from django.contrib import admin
# Create your models here.

class Employee (models.Model):
    EMP_ID=models.CharField(primary_key=True,max_length=3,help_text="Phonenumber")
    Name=models.CharField(max_length=100)
    Post=models.CharField(max_length=30)
    Salary=models.IntegerField()
    Email=models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('EMP_ID','Name','Post','Salary','Email')