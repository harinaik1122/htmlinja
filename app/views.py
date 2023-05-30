from django.shortcuts import render

# Create your views here.
def home(request):
    b={'a':10, 'd':30}
    return render(request,'home.html',context=b)
