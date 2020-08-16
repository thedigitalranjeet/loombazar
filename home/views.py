from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'home/index.html')

def product_details(request):
    return render(request,'home/product_details.html')

