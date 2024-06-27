from django.db import models

# Create your models here.
class Course_db(models.Model):
    student_id=models.CharField(max_length=20)
    student_name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    marks=models.IntegerField()

    def __str__(self):
        return f"{self.student_id} has secured {self.marks} in {self.subject}"
