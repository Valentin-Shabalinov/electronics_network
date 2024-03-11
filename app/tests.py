from django.test import TestCase
from .models import Supplier

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class SupplierModelTests(TestCase):
    def test_supplier_creation(self):
        """Тестирование создания поставщика"""
        supplier = Supplier(
            name="Test Supplier",
            email="test@example.com",
            country="Country",
            city="City",
            street="Street",
            house_number="123",
            address="Full Address",
        )
        supplier.save()
        self.assertIs(
            Supplier.objects.filter(name="Test Supplier").exists(), True
        )


class SupplierAPITests(APITestCase):
    def setUp(self):
        # Создание тестового пользователя
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", is_active=True
        )

    def test_create_supplier(self):
        """Тестирование создания поставщика через API"""
        self.client.login(
            username="testuser", password="testpassword"
        )  # Аутентификация
        url = reverse("supplier-list")
        data = {
            "name": "New Supplier",
            "email": "supplier@example.com",
            "country": "Country",
            "city": "City",
            "street": "Street",
            "house_number": "123",
            "address": "Full Address",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(Supplier.objects.get().name, "New Supplier")
