import json
# import stripe
from django.shortcuts import render, redirect

from django.conf import settings
from django.http import JsonResponse
from .models import Order, OrderItem
from cart.cart import Cart 
from table.models import Table
def start_order(request):
    cart = Cart(request)
    # print(request.body)
    data = json.loads(request.body)
    # print(data)
    total_price = 0
    items = []

    for item in cart:
        if int(item['quantity']) <= 0:
            return False
        product = item['product']
        total_price += product.price * int(item['quantity'])

        items.append({
            'price_data': {
                'currency': 'tnd',
                'product_data': {
                'name': product.name,
                },
                'unit_amount': product.price,
            },
            'quantity': item['quantity']
        })

        order = Order.objects.create(
            user=request.user,
            table=Table.objects.get(table_number=int(data['table_number'])),
            first_name=data['first_name'],
            email=data['email'],
            phone=data['phone'],
            paid = False,
            paid_amount = total_price)

        order.save()

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        cart.clear()

        return JsonResponse({'success': True})

def order_list(request):
    orders=Order.objects.all().order_by('created_at')
    query={}
    for o in orders :
        items=OrderItem.objects.filter(order_id=o.id)
        query[o.id]={
            'order':o,
            'items':items}
        print(query)
    return render(request,'pages/order_list.html',{'orders':orders,'query':query})

def item_ready(request,id):
    item=OrderItem.objects.get(id=id)
    if item.ready:
        item.ready=False
    else:
        item.ready = True
    item.save()

