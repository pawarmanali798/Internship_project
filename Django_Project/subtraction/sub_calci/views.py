from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sub(request):
    if request.method=='POST':
        num1=request.POST.get('number1',0)
        num2=request.POST.get('number2',0)
        result=int(num1) - int(num2)
        return HttpResponse(result)
    return render(request,'sub_calci.html')
