import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Mocha", 3.00, 3)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("Mocha", self.drink.name)