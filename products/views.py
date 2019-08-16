from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.

def product_list(request):
	products = Product.objects
	return render(request,'product_list.html',{"products": products})

def detail(request,product_id):
	product = get_object_or_404(Product,pk=product_id)
	return render(request,'detail.html',{'product': product})


@login_required
def publish(request):
	if request.method == 'GET':
		return render(request,'publish.html')
	elif request.method == 'POST':
		title = request.POST['title']
		intro = request.POST['intro']
		url = request.POST['url']
		# try:
		icon = request.FILES['icon']
		image = request.FILES['image']
			
		product = Product()
		product.title = title
		product.intro = intro
		product.url = url
		product.icon = icon
		product.image = image
			
		product.pub_date = timezone.datetime.now()
		product.hunter = request.user
		product.save()

	return redirect('home')

		# except Exception as err:
		# 	return render(request,'publish.html',
		# 		{'错误':'请上传图片'})