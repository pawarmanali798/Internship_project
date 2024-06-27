from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

class StudentView(APIView):
    def get(self, request):
        data = Student.objects.all() # data from db
        serialized_data = StudentSerializer(data, many=True) # JSON data
        return Response(serialized_data.data)
    
    def post(self,request):#create
        mydata = request.data
        serialized = StudentSerializer(data = mydata)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = 201)
        return Response(serialized.errors, status = 400)
    
    def put(self,request,rollno=None):#update
        student1=Student.objects.get(rollno=rollno)
        serialized=StudentSerializer(student1,data=request.data)
        if serialized.is_valid():
            serialized.save()
        return Response("{'message':'updated}")
    
    def delete(self,request,rollno = None):
        data1=Student.objects.get(rollno=rollno)
        data1.delete()
        return Response("{'message':'deleted'}")
