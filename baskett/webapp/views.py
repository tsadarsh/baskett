from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Product, Category


@login_required
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

def order(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	print(request.POST)
	ordered = int(request.POST['number'])
	product.quantity -= ordered
	product.save()

	return HttpResponseRedirect(reverse('webapp:detail', args=[product_id]))