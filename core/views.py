from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import mail
from django.contrib import messages
from product.models import Category, Product
from django.conf import settings
import os
from cart.forms import CartAddProductForm

def frontpage(request):
    list=[]
    categories = Category.objects.all().order_by('id')
    products = Product.objects.all()
    for cat in categories:
        produitsFiltre=products.filter(category=cat)
        obj={
            "cat":cat,
            "products":produitsFiltre,
            "nbProduits":produitsFiltre.count(),
        }
        list.append(obj)
    form = CartAddProductForm()
    return render(request, 'new/index.html',{'products':products,'form':form,'list':list,"categories":categories,})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        message = request.POST.get('message')

        if name != '' and email_from != '' and message != '':

            with mail.get_connection() as connection:
                mail.EmailMessage(f"Contact Request: {name} {email_from}", message, email_from, ['TTT@gmail.com'], connection=connection,).send()
                messages.success(request, "Message Sent!")

        else:
            messages.error(request, "Error!")
            
    return render(request, 'core/contact.html')

@login_required
def myaccount(request):
    return render(request, 'core/my_account.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

def shop(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'core/shop.html', context)
