from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def add(request):
    # return redirect('http://www.google.com') & import redirect
    if request.method=='POST':
        num1=request.POST.get('number1',0)
        num2=request.POST.get('number2',0)
        result=int(num1) + int(num2)
        return HttpResponse(result)
    return render(request,'add_calci.html')

    