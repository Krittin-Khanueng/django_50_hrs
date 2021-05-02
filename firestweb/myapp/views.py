from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Allproduct, Profile

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
    if request.user.profile.usertype != 'admin':
        return redirect('home-page')

    if request.method == 'POST' and request.FILES['imageupload']:
        data = request.POST.copy()
        name = data.get('name')
        price = data.get('price')
        detail = data.get('detail')
        imageurl = data.get('imageurl')
        quantity = data.get('quantity')
        unit = data.get('unit')

        new = Allproduct()
        new.name = name
        new.price = price
        new.detail = detail
        new.imageurl = imageurl
        new.quantity = quantity
        new.unit = unit
        ######## save Image###############
        file_image = request.FILES['imageupload']
        file_image_name = request.FILES['imageupload'].name.replace(' ', '')
        print('FILE_IMAGE:', file_image)
        print('FILE_IMAGE:', file_image.name)
        fs = FileSystemStorage()
        filename = fs.save(file_image_name, file_image)
        upload_file_url = fs.url(filename)
        new.image = upload_file_url[6:]
        #######################
        new.save()

    return render(request, 'myapp/addproduct.html')


def Product(request):
    product = Allproduct.objects.all().order_by('id').reverse()
    context = {'product': product}
    return render(request, 'myapp/allproduct.html', context)


def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.email = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.set_password(password)
        newuser.save()

        profile = Profile()
        profile.user = User.objects.get(username=email)
        profile.save()

        user = authenticate(username=email, password=password)
        login(request, user)

    return render(request, 'myapp/register.html')
