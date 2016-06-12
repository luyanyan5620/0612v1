from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from mhdb.forms import OrdersForm
from django.shortcuts import redirect
import json
from jsonview.decorators import json_view
# Create your views here.

# @json_view
# def my_view(request):
#     return {
#         'foo': 'bar',
#     }
@json_view
def home(request):
    return {
        'foo': 'bar',
    }


def orders_add(request):

    if request.method == 'POST':

        form = OrdersForm(request.POST)
        if form.is_valid():
           order_info = form.save()
           order_info.save()
        return HttpResponse('Thank you')
         #  redirect('views.order_details')

    else:
        form = OrdersForm()
    return render(request, 'mhdb/orders_add.html', {'form_info': form})


def order_details(request):

    return HttpResponse('order add success!')
    
