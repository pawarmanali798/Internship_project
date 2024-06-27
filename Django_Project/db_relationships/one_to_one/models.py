from django.db import models

# Create your models here.


# models.py



class Address(models.Model):
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)

    def __str__(self):
        return "City:" + self.city + " with pincode:" + self.pincode

class Employee(models.Model):
    empid = models.CharField(max_length=10)
    empname = models.CharField(max_length=50)
    salary = models.CharField(max_length=30, default='0')
    address = models.ForeignKey(Address,on_delete=models.CASCADE, related_name="employee")
    
    def __str__(self):
        return "Empid:"+self.empid+ "Empname:"+self.empname+ "salary:" +self.salary+"address"+self.address