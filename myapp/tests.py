from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name= 'Test Product',
            price= 9.99,
            description= 'This is a test product.')
        
        
    def test_get_products(self):
        url=reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        
    def test_create_product(self):
        url=reverse('product-list')
        data = {
            'name': 'New Product',
            'price': 19.99,
            'description': 'This is a new product.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_update_product(self):
        url=reverse('product-detail', args=[self.product.id])
        data = {
            'name': 'Updated Product',
            'price': 29.99,
            'description': 'This is an updated product.'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        
        
    def test_delete_product(self):
        url=reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())



        
        
        