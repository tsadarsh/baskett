from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Product
from .models import Category
from .models import History


def home(request):
	"""Home page lists the categories available to choose from"""
	categories = Category.objects.all()
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

@login_required
def order(request, product_id):
	"""Order is placed, stock quantity is reduced and new record in 
	history is made.
	"""
	product = get_object_or_404(Product, pk=product_id)
	if product.seller.available:
		ordered = int(request.POST['number'])
		if ordered <= product.quantity:
			product.quantity -= ordered
			product.save()

			History.objects.create(
				item = product,
				buyer = request.user,
				quantity = ordered
			)

	else:
		pass
	return HttpResponseRedirect(reverse('webapp:detail', args=[product_id]))

@login_required
def history(request):
	"""The orders placed by the User is retreived from the DB. """
	user = request.user
	user_buy_history = History.objects.filter(buyer__exact=user)
	return render(
		request, 
		'webapp/history.html', 
		{
			'user_buy_history': user_buy_history,
			'user': user
		}
	)

def remove_seller(request):
	s = request.POST['name']
	seller = Seller.objects.filter('s__exact')
	seller.available = False