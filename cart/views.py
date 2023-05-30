from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .cart import Cart
from product.models import Product
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from django.http import JsonResponse

# @require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartAddProductForm(request.POST)
    # print(form.errors)
    if form.is_valid():
        # print("valide")
        cd=form.cleaned_data
        cart.add(product_id=product_id,quantity=cd['quantity'],update_quantity=cd['override'])
    return redirect('cart:cart_detail')
# @require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    # product = get_object_or_404(Product,id=product_id)
    cart.remove(product_id)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # print(cart.cart)
    form = CartAddProductForm()
    # return render(request, 'new/index.html',{'products':products,'form':form,})
    return JsonResponse(cart.cart)


# def update_cart(request, product_id, action):
#     cart = Cart(request)
#     if action == 'increment':
#         cart.add(product_id, 1, True)
#     else:
#         cart.add(product_id, -1, True)
#
#     product = Product.objects.get(pk=product_id)
#     quantity = cart.get_item(product_id)
#
#     if quantity:
#         quantity = quantity['quantity']
#
#         item = {
#             "product": {
#             "id": product.id,
#             "name": product.name,
#             "image": product.image,
#             "get_thumbnail": product.get_thumbnail(),
#             "price": product.price,
#             },
#             "total_price": (quantity * product.price),
#             "quantity": quantity,
#         }
#         print(item)
#     else:
#         item = None
#
#     response = render(request, 'pages/cart_item.html', {'item': item})
#     response["HX-Trigger"] = 'update-menu-cart'
#
#     return response
#
# def hx_menu_cart(request):
#     return render(request, 'cart/menu_cart.html')
#
# def hx_cart_total(request):
#     return render(request, 'pages/cart_total.html')
#
# def cart(request):
#     return render(request, 'cart/cart.html')
#
# def success(request):
#     return render(request, 'cart/success.html')
#
# @login_required
# def checkout(request):
#     # pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
#     return render(request, 'pages/home.html', {})

