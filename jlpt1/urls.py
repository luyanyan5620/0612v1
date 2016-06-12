from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='jlpt1'
urlpatterns = [
     url(r'^$',views.home,name='index'),

     url(r'^recv_data/$',views.recv_data,name='recv_data'),
     url(r'^my_view/$',views.my_view,name='my_view'),
     #url(r'^jsonResponse/$',views.jsonResponse,name='index'),
]
