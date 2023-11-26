from django.urls import path
from . import views 

urlpatterns = [
	path('', views.access, name="access"),
	path('home', views.home, name="home"),
	path('configuration', views.configuration, name="configuration"),
	path('dataOptionSelector', views.dataOptionSelector, name="dataOptionSelector"),
	path('obtener_ultimo_dato/', views.obtener_ultimo_dato, name='obtener_ultimo_dato'),

] 	