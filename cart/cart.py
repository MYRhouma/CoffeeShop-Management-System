from django.conf import settings

from product.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {'cart': {},
                                                             'discount':0.0}

        self.cart = cart['cart']
        self.discount = cart['discount']

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = float(item['product'].price * item['quantity'])
            yield item

    
    def __len__ (self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID]['cart'] = self.cart
        self.session[settings.CART_SESSION_ID]['discount'] = self.discount
        self.session.modified = True
    
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        product=Product.objects.get(pk=product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'id': product_id, 'name':product.name,'price_unit':product.price,'image_url':product.image.url,}
        else:
            self.cart[product_id]['quantity'] +=1
        if update_quantity:
            self.cart[product_id]['quantity'] = int(quantity)

            if self.cart[product_id]['quantity'] <= 0:
                self.remove(product_id)

        self.save()
    
    def remove(self, product_id):
        if str(product_id) in self.cart:
            del self.cart[str(product_id)   ]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return sum(float(item['product'].price * item['quantity']) for item in self.cart.values())
    
    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None
    def set_discount(self, value):
        self.discount=float(value)
        self.save()
