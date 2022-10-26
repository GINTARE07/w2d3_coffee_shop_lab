import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.food import Food
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Binary Bean", 500.00)

        self.coffee_shop.new_drink(Drink("Mocha", 2.50, 2), 15)
        self.coffee_shop.new_drink(Drink("Latte", 3.50, 3), 12)
        self.coffee_shop.new_drink(Drink("Hot Chocolate", 3.00, 0), 40)
        self.coffee_shop.new_drink(Drink("tea", 2.00, 0), 6)

        self.customer_1 = Customer("Bart", 50.00, 18, 3)
        self.customer_2 = Customer("Marge", 50.00, 42, 8)
        self.customer_3 = Customer("Lisa", 50.00, 14, 3)
        self.customer_4 = Customer("Homer", 50.00, 45, 11)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Binary Bean", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(500.00, self.coffee_shop.till)
    
    def test_add_drink(self):
        self.assertEqual(4, len(self.coffee_shop.drinks))

    def test_buy_drink(self):
        self.customer_1.buy_drink(self.coffee_shop.select_drink("Mocha"))
        self.coffee_shop.increase_till(self.coffee_shop.select_drink("Mocha"))
        self.assertEqual(502.50, self.coffee_shop.till)
        self.assertEqual(47.50, self.customer_1.wallet)
    
    def test_age_check(self):
        self.assertEqual(True, self.coffee_shop.check_age(self.customer_2, self.coffee_shop.select_drink("Mocha")))
        self.assertEqual(False, self.coffee_shop.check_age(self.customer_3, self.coffee_shop.select_drink("Mocha")))
    
    def test_increase_energy_level(self):
        self.customer_1.increase_energy_level(self.coffee_shop.select_drink("Mocha"))

        self.assertEqual(5, self.customer_1.energy_level)
    
    def test_energy_level_too_high(self):
        self.assertEqual(True, self.coffee_shop.energy_level_too_high(self.customer_4))
        self.assertEqual(False, self.coffee_shop.energy_level_too_high(self.customer_2))
    
    def test_decrease_energy_level(self):
        self.customer_4 = Customer("Homer", 50.00, 45, 6)
        steak = Food("Steak", 15.00, 3)
        self.customer_4.decrease_energy_level(steak)

        self.assertEqual(3, self.customer_4.energy_level)
    
    def test_stock_value(self):
        self.assertEqual(211.5, self.coffee_shop.stock_value())
