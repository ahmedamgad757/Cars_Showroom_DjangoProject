from django.shortcuts import render
from .models import NewCar,UsedCar
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def newcars(request):
    return render(request,'pages/newcars.html',{'Ncars':NewCar.objects.all()})

def usedcars(request):
    return render(request,'pages/usedcars.html',{'Ucars':UsedCar.objects.all()})

def sell(request):
    return render(request,'pages/sellyourcar.html')