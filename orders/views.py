from django.shortcuts import render
from .models import Order,OrderItem
from .forms import OrderForm
from cart.cart import Cart



def order_create(request):
    cart= Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST, request=request)
        if form.is_valid():
            order = form.save(commit=False)
            for item in cart:
                OrderItem.objects.create(order=order, product =item['product'],price=item['price'],quantity=item['quantity'])

            cart.clear()
            return render(request,'order/create.html',
                          {'form': form, 'order': order})
        else:
            form = OrderForm(request=request)
            return render (request,
                           'order/create.html',
                           {'form': form, 'cart': cart})
