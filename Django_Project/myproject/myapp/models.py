from django.db import models

class Student(models.Model):
    rollno=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    marks=models.IntegerField()