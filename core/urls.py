from django.urls import path, include
from .views import frontpage, shop, myaccount, edit_myaccount, contact

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('contact/', contact, name='contact'),
    path('myaccount/', myaccount, name='myaccount'),
    path('edit_mcaccount/', edit_myaccount, name='edit_myaccount'),
    path('shop', shop, name='shop'),
    path('accounts/', include('allauth.urls')),
]
