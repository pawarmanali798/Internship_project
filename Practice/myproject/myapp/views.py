from django.shortcuts import render, HttpResponse

# ... other code ...

def form(request):
    if request.method == 'POST':
        fname = request.POST.get('firstName', None)
        prn_no = request.POST.get('prn', 0)
        email = request.POST.get('emailID', None)
        password = request.POST.get('pass', None)
        context = {
            "firstName": fname,
            "prn": prn_no,
            "emailID": email,
            "pass": password,
        }
        return render(request,'views.html', context)
    else:
        # Handle GET request explicitly
        return render(request,'views.html')  # You might want to pass an empty context or a specific message