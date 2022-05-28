from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def home(request):
	"""Home page lists the categories available to choose from"""
	categories = Category.objects.all
	return render(request, 'webapp/home.html', {'categories': categories})

def index(request, category):
	"""Returns products that match the category provied. If category is
	'all' then return all the products from DB.
	"""
	if category == "all":
		products = Product.objects.all()
	else:
		category_id = Category.objects.filter(category=category)[0].id
		products = Product.objects.filter(category=category_id)

	return render(request, 'webapp/index.html', {'products': products})

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'webapp/detail.html', {'product': product})