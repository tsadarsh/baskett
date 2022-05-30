from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
	path('login_auth/', views.login_auth, name="login_auth"),
	path('login/', views.login, name="login"),
	path('signup/', views.signup, name="signup"),
	path('signup_auth/', views.signup_auth, name="signup_auth"),
]