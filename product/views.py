from django.shortcuts import render
from product.models import Product

def product(request, slug):
    products = Product.objects.all()

    products = products.filter(category__slug=slug)

    context = {
        'products': products
    }    

    
    return render(request, 'product/product.html', context)
    # return render(request, 'pages/home.html', context)


def product_detail(request, id):
    
    
    product = Product.objects.get(id=id)
    
    context = {
        'product': product
    }
    
    return render(request, 'product/product_detail.html', context)
