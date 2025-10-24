from django.test import TestCase
from .models import Menu

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Test Dish",
            price=12.99,
            inventory=50
        )
    
    def test_menu_creation(self):
        """Test that menu item is created correctly"""
        self.assertEqual(self.menu_item.title, "Test Dish")
        self.assertEqual(self.menu_item.price, 12.99)
        self.assertEqual(self.menu_item.inventory, 50)