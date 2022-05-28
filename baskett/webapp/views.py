from django.shortcuts import render, get_object_or_404

from .models import Product

def index(request):
	products = Product.objects.all
	return render(request, 'webapp/index.html', {'products': products})

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'webapp/detail.html', {'product': product})