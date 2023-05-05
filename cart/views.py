from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .cart import Cart
from product.models import Product

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            "product": {
            "id": product.id,
            "name": product.name,
            "image": product.image,
            "get_thumbnail": product.get_thumbnail(),
            "price": product.price,
            },
            "total_price": (quantity * product.price),
            "quantity": quantity,
        }
        print(item)
    else:
        item = None

    response = render(request, 'pages/cart_item.html', {'item': item})
    response["HX-Trigger"] = 'update-menu-cart'  

    return response

def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'pages/cart_total.html')

def cart(request):
    return render(request, 'pages/home.html')

def success(request):
    return render(request, 'cart/success.html')

@login_required
def checkout(request):
    # pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    return render(request, 'pages/home.html', {})

