from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
	"""Each product comes under one seller

	Example: Big Basket"""
	seller_name = models.CharField(max_length=200, unique=True)
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.seller_name

class Category(models.Model):
	"""Each product comes under one category

	Example: Fruits
	"""
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class Item(models.Model):
	name = models.CharField(max_length=100)

class Product(models.Model):
	"""Describes the Item attributes"""
	seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
	product_name = models.ForeignKey(Item, on_delete=models.PROTECT)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)

	def __str__(self):
		return self.product_name

class History(models.Model):
	"""Displays the history of oders placed by the User """
	item = models.ForeignKey(Product, on_delete=models.SET_NULL)
	buyer = models.ForeignKey(User, on_delete=models.SET_NULL)
	quantity = models.IntegerField(default=0)
