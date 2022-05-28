from django.db import models

class Seller(models.Model):
	"""Each product comes under one seller

	Example: Big Basket"""
	seller_name = models.CharField(max_length=200)

	def __str__(self):
		return self.seller_name

class Category(models.Model):
	"""Each product comes under one category

	Example: Fruits
	"""
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class Product(models.Model):
	"""Describes the product attributes"""
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=300)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# product_img = models.ImageField()
	quantity = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)

	def __str__(self):
		return self.product_name