from django.urls import path
from . import views 

urlpatterns = [
	path('', views.access, name="access"),
	path('home', views.home, name="home"),
	path('configuration', views.configuration, name="configuration"),
	path('dataOptionSelector', views.dataOptionSelector, name="dataOptionSelector")

] 	