from django.shortcuts import render

# Create your views here.



def nike(request):
    return render(request,'nike.html')

def adidas(request):
    return render(request,'adidas.html')
