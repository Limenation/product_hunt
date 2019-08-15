from django.shortcuts import render

# Create your views here.

def product_list(request):
	return render(request,'product_list.html')

def publish(request):
	return render(request,'publish.html')