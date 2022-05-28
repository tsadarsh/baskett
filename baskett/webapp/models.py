from django.db import models

# Create your models here.
class Seller(models.Model):
	seller_name = models.CharField(max_length=200)

	def __str__(self):
		return self.seller_name

class Category(models.Model):
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.category

class Product(models.Model):
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=300)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# product_img = models.ImageField()
	rating = models.IntegerField(default=0)

	def __str__(self):
		return self.product_name