from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
	path("", views.home, name="home"),
	path("<str:category>/", views.index, name="index"),
	path("product/<int:product_id>/", views.detail, name="detail"),
	path("product/<int:product_id>/order/", views.order, name="order"),
]