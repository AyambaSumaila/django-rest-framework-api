from django.shortcuts import render
from rest_framework import generics  # type: ignore
from.models import Product
from.serializers import ProductSerializer
from django.views.generic import ListView, DetailView  # type: ignore

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(ListView):
    model = Product
    template_name='product_list.html'
    
    
    

class ProductDetailView(DetailView):
    model = Product
    template_name='product_detail.html'