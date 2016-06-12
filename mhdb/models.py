# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


OS_CHOICES = (
    ('N1', 'N1'),
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
    ('N5', 'N5'),
    ('NO', 'NO'),
)
DEVICE_STATUS = (
    ('N1', 'N1'),
    ('N2', 'N2'),
    ('N3', 'N3'),
    ('N4', 'N4'),
    ('N5', 'N5'),
    ('NO', 'NO'),
)
# Create your models here.
@python_2_unicode_compatible
class Orders(models.Model):
    requester = models.CharField(max_length=20)
    costcenter = models.CharField(max_length=20)
    project = models.CharField(max_length=20)
    owner = models.EmailField(max_length=254) #邮件格式
    label= models.CharField(max_length=20)# 下拉菜单提示，有api么
    order_date =models.DateTimeField('date ordered')


    def __str__(self):
            return self.requester

@python_2_unicode_compatible
class Order_details(models.Model):
    device= models.CharField(max_length=20)
    os= models.CharField(max_length=20) #下拉菜单选择
    orders=models.ForeignKey('Orders')
    quantity =models.IntegerField(default=0)

    def __str__(self):
            return self.device

@python_2_unicode_compatible
class Devices(models.Model):
    device_seri_number=models.IntegerField()
    
    device_name= models.CharField(max_length=20)
    device_os= models.CharField(max_length=20, choices=OS_CHOICES) #下拉菜单选择
    device_quantity =models.IntegerField(default=1)
    
    requester = models.CharField(max_length=20)
    costcenter = models.CharField(max_length=20)
    project = models.CharField(max_length=20)
    owner = models.EmailField(max_length=254) #邮件格式
    label= models.CharField(max_length=20)# 下拉菜单提示，有api么
    add_date =models.DateTimeField('date for device addin')
    device_status =models.CharField(max_length=20, choices=DEVICE_STATUS)

    def __str__(self):
            return self.device_name
