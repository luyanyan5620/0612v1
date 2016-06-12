from django.contrib import admin
from mhdb.models import Orders,Devices
# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['requester', 'project']
admin.site.register(Orders, OrdersAdmin)

class DevicesAdmin(admin.ModelAdmin):
    list_display = ['device_seri_number','device_name','device_os','requester', 'project','costcenter',]
admin.site.register(Devices, DevicesAdmin)
