from django.test import TestCase
from ..models import Menu
from ..serilaizers import menuSerializer
from django.urls import reverse
from rest_framework.test import APIClient

class MenuItemTest(TestCase):
    def setUp(self):
        # Create some MenuItem test data
        self.item1 = Menu.objects.create(Title="Pizza", Price=50, Inventory=10)
        self.item2 = Menu.objects.create(Title="Burger", Price=30, Inventory=20)
        self.item3 = Menu.objects.create(Title="Pasta", Price=40, Inventory=15)

        self.client = APIClient()

    def test_getall(self):
        url = reverse("menu-list")
        response = self.client.get(url)

        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)


        self.assertEqual(response.status_code, 401)
        # self.assertEqual(response.data, serializer.data)

    def test_get_item(self):
        item=Menu.objects.create(Title='IceCream',Price=80,Inventory=100)
        self.assertEqual(str(item),"IceCream : 80")