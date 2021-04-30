from django.shortcuts import render
from django.http import HttpResponse
from .models import Allproduct


def Home(request):
    product1 = 'แอปเปิ้ลเขียว'
    product2 = 'องุ่น'
    product3 = 'ทุเรียน'
    context = {'product1': product1, 'product2': product2, 'product3': product3}
    return render(request, 'myapp/home.html', context)


def About(request):
    return render(request, 'myapp/about.html')


def Contact(request):
    return render(request, 'myapp/contact.html')


def AddProduct(request):
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        price = data.get('price')
        detail = data.get('detail')
        imageurl = data.get('imageurl')

        new = Allproduct()
        new.name = name
        new.price = price
        new.detail = detail
        new.imageurl = imageurl
        new.save()

    return render(request, 'myapp/addproduct.html')
