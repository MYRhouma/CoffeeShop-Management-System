from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    #CART
    path("",views.cart_detail,name="cart_detail"),
    path("add/<int:product_id>",views.cart_add,name="cart_add"),
    path("remove/<int:product_id>",views.cart_remove,name="cart_remove"),
    path("clear/",views.cart_clear,name="cart_clear"),
    #DISCOUNTS
    path("set_cart_discount/", views.set_cart_discount, name="set_cart_discount"),



    #OLD
    # path("", cart, name='cart'),
    # path("checkout/", checkout, name='checkout'),
    # path("success/", success, name="success"),
    # path("add_to_cart/<int:product_id>/", add_to_cart, name='add_to_cart'),
    # path("update_cart/<int:product_id>/<str:action>", update_cart, name="update_cart"),
    # path("hx_menu_cart", hx_menu_cart, name='hx_menu_cart'),
    # path("hx_cart_total", hx_cart_total, name='hx_cart_total'),
]