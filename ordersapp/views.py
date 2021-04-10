from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from .models import Order, OrderItem
from .forms import OrderFormItem
from basketapp.models import Basket


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Заказы'
        return context

    # @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(OrderList, self).dispatch(request, *args, **kwargs)


class OrderItemsCreat(CreateView):
    model = Order
    fields = []
    context_object_name = 'object'
    success_url = reverse_lazy('orders:order_list')

    def get_context_data(self, **kwargs):
        context = super(OrderItemsCreat, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Создать заказ'
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderFormItem, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if len(basket_items):
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderFormItem, extra=len(basket_items))
                formset = OrderFormSet()

                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                basket_items.delete()
            else:
                formset = OrderFormSet()

        context['orderitems'] = formset
        return context

    # @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/'))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(OrderItemsCreat, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        # удаляем пустой заказ
        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsCreat, self).form_valid(form)


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order_list')



class OrderRead(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderRead, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Просмотр заказа'
        return  context



def order_forming_complete(request,pl):
    order = get_object_or_404(Order,pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('orders:order_list'))