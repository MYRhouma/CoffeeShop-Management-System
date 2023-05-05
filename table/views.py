from django.shortcuts import render

# Create your views here.
def table_scan(request):
    return render(request,'scan_qrcode.html')