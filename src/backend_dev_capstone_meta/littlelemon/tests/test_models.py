from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Pizza Margherita", price=12, inventory=1000)
        itemstr = item.__str__()

        self.assertEqual(itemstr, "Pizza Margherita : 12")