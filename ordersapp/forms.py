from django import forms

from mainapp.models import Product
from .models import Order,OrderItem


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderFormItem(forms.ModelForm):
    price = forms.CharField(label='цена',required=False)
    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrderFormItem, self).__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['product'].queryset = Product.get_items()