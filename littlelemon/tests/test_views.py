from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework import status
from rest_framework.test import APIClient

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(name="Menu 1", description="Description for Menu 1", price=10.99)
        self.menu2 = MenuItem.objects.create(name="Menu 2", description="Description for Menu 2", price=15.99)
        self.menu3 = MenuItem.objects.create(name="Menu 3", description="Description for Menu 3", price=20.99)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
