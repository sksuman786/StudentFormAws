

from django.http import HttpResponse


def home(request):
	x = "I am Sk Suman" 

	return HttpResponse (x)