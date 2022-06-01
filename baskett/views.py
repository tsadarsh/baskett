from django.http import HttpResponseRedirect
from django.urls import reverse

def welcome_page(request):
	return HttpResponseRedirect(reverse('webapp:home'))