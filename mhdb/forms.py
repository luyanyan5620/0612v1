from django.forms import ModelForm
from mhdb.models import Orders,Order_details

# create your ..
class OrdersForm(ModelForm):
    class Meta:
        model = Orders #reference  which models you want
        fields = '__all__'
        #exclude =('order_date',)
