from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Product, Category, Seller

class OrderingTests(TestCase):
	def test_user_logged_in_before_placcing_order(self):
		sample_seller = Seller.objects.create(
			seller_name = "Foo market"
		)
		sample_category = Category.objects.create(
			category = "Sample category"
		)
		sample_product = Product.objects.create(
			seller = sample_seller,
			product_name = "Sample Item",
			category = sample_category,
			quantity = 10,
			rating = 5
		)

		response = self.client.get(reverse('webapp:home'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context, [sample_category])

class UserSignup(TestCase):
	def __init__(self):
		self.username = 'test_user'
		self.password = 'test_password'
		self.email = 'testemail@email.com'

	def create_user(self, username=self.username,
					email=self.email, password=self.password):
		user = User.objects.create_user(
			username, email, password
		)

	def test_user_signup_with_already_existing_username(self):
		user1 = self.create_user()
		user2 = self.create_user()