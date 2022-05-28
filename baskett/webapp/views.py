from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def home(request):
	categories = Category.objects.all
	return render(request, 'webapp/home.html', {'categories': categories})

def index(request, category):
	category_id = Category.objects.filter(category=category)[0].id
	products = Product.objects.filter(category=category_id)
	return render(request, 'webapp/index.html', {'products': products})

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'webapp/detail.html', {'product': product})