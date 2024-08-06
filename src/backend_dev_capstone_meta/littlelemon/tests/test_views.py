from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        # Adding test instances of the Menu model
        self.menu1 = MenuItem.objects.create(title='Pizza', price=9.99, inventory=10)
        self.menu2 = MenuItem.objects.create(title='Burger', price=5.99, inventory=300)
        self.menu3 = MenuItem.objects.create(title='Pasta', price=7.99, inventory=22)

    def test_getall(self):
        # Retrieving all Menu objects
        menus = MenuItem.objects.all()
        # Serializing the retrieved objects
        serializer = MenuItemSerializer(menus, many=True)
        # Expected serialized data
        expected_data = [
            {
                'id': self.menu1.id,
                'title': self.menu1.title,
                'price': str(self.menu1.price),  # Decimal to string for serialization match
                'inventory': self.menu1.inventory,
            },
            {
                'id': self.menu2.id,
                'title': self.menu2.title,
                'price': str(self.menu2.price), 
                'inventory': self.menu2.inventory, 
            },
            {
                'id': self.menu3.id,
                'title': self.menu3.title,
                'price': str(self.menu3.price), 
                'inventory': self.menu3.inventory, 
            }
        ]
        # Running assertions to check if the serialized data equals the response
        self.assertEqual(serializer.data, expected_data)
