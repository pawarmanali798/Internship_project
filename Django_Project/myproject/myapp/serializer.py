from rest_framework import serializers
from myapp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # rollno=serializers.CharField(max_length=50)
    # sname=serializers.CharField(max_length=50)
    # marks=serializers.IntegerField()

    class Meta:
        model = Student
        fields = '__all__'