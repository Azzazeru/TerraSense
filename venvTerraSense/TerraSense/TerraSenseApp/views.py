from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

TEMPLATE_DIRS = (
	'os.path.join(BASE_DIR, "templates"),'
)

def access(request):
	return render(request, "access.html")

def home(request):
	return render(request, "home.html")

def configuration(request):
	return render(request, "configuration.html")

def dataOptionSelector(request):
	return render(request, "dataOptionSelector.html")