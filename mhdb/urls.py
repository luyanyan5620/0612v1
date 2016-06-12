from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='mhdb'
urlpatterns = [
     url(r'^$',views.home,name='index'),
     url(r'^orders_add/$',views.orders_add,name='orders'),
     url(r'^order_details/$',views.order_details,name='details'),
	#url(r'^jsonResponse/$',views.jsonResponse,name='index'),
]
