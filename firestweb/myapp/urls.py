from django.urls import path, include
from .views import Home, About, Contact, AddProduct, Product

urlpatterns = [
	path('', Home, name='home-page'),
	path('about/', About, name='about-page'),
	path('contact/', Contact, name='contact-page'),
	path('addproduct/', AddProduct, name='addproduct-page'),
	path('allproduct/', Product, name='allproduct-page')
]
