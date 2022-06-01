from django.shortcuts import render
from django.contrib.auth import authenticate as dj_auth
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
	return render(request, 'accounts/login.html')

def login_auth(request):
	username = request.POST['uname']
	password = request.POST['passwd']
	user = dj_auth(
		request,
		username=username,
		password=password
	)

	if user is not None:
		dj_login(request, user)
		return HttpResponseRedirect(reverse('webapp:home'))

	else:
		error_message = "Incorrect credentials!"
		return render(
			request,
			'accounts/login.html',
			{'error_message': error_message}
		)

def signup(request):
	return render(request, 'accounts/signup.html')

def signup_auth(request):
	username = request.POST['uname']
	email = request.POST['email']
	password = request.POST['passwd']
	password_confirm = request.POST['passwd_conf']

	# Check if the username is unique

	if len(User.objects.filter(username__exact=username)) != 0:
		return render(
			request,
			'accounts/signup.html',
			{'error_message': 'Username is not unique'}
		)

	# Check if email ID is unique

	if len(User.objects.filter(email__exact=email)) != 0:
		return render(
			request,
			'accounts/signup.html',
			{'error_message': 'Email ID already in use'}
		)

	# Check if passwords match

	if password != password_confirm:
		return render(
			request,
			'accounts/signup.html',
			{'error_message': 'Passwords do not match'}
		)
	User.objects.create_user(username, email, password)
	return render(request, 'accounts/login.html')

def logout_view(request):
	logout(request)
	return render(request, 'accounts/login.html')
