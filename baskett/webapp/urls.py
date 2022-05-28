from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
	path("", views.home, name="home"),
	path("<str:category>/", views.index, name="index"),
	path("<int:product_id>/", views.detail, name="detail"),
]