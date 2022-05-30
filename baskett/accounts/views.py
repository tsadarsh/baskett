from django.shortcuts import render
from django.contrib.auth import authenticate as dj_auth
from django.contrib.auth import login as dj_login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
	return render(request, 'accounts/login.html')

def auth(request):
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