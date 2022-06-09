from django.contrib import admin

from .models import Seller
from .models import Product
from .models import Category
from .models import Item

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Item)
