from django.test import TestCase
from restaurant.models import MenuItem, Booking
from decimal import Decimal
from datetime import datetime

class MenuItemTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pizza", price=Decimal('12.99'), inventory=10)
        MenuItem.objects.create(title="Pasta", price=Decimal('9.99'), inventory=5)

    def test_menu_item_price(self):
        pizza = MenuItem.objects.get(title="Pizza")
        pasta = MenuItem.objects.get(title="Pasta")
        self.assertEqual(pizza.price, Decimal('12.99'))
        self.assertEqual(pasta.price, Decimal('9.99'))

    def test_menu_item_inventory(self):
        pizza = MenuItem.objects.get(title="Pizza")
        pasta = MenuItem.objects.get(title="Pasta")
        self.assertEqual(pizza.inventory, 10)
        self.assertEqual(pasta.inventory, 5)

class BookingTestCase(TestCase):
        def setUp(self):
            Booking.objects.create(name="John", no_of_guests=5, booking_date=datetime.now())
            Booking.objects.create(name="Jane", no_of_guests=10, booking_date=datetime.now())
    
        def test_booking_name(self):
            john = Booking.objects.get(name="John")
            jane = Booking.objects.get(name="Jane")
            self.assertEqual(john.name, "John")
            self.assertEqual(jane.name, "Jane")
    
        def test_booking_guests(self):
            john = Booking.objects.get(name="John")
            jane = Booking.objects.get(name="Jane")
            self.assertEqual(john.no_of_guests, 5)
            self.assertEqual(jane.no_of_guests, 10)
