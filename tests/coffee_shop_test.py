import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.food import Food
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Binary Bean", 500.00)

        mocha = Drink("Mocha", 2.50, 2)
        latte = Drink("Latte", 3.50, 3)
        hot_chocolate = Drink("Hot Chocolate", 3.00, 0)
        tea = Drink("tea", 2.00, 0)
        self.coffee_shop.new_drink(mocha, 15)
        self.coffee_shop.new_drink(latte, 12)
        self.coffee_shop.new_drink(hot_chocolate, 40)
        self.coffee_shop.new_drink(tea, 6)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Binary Bean", self.coffee_shop.name)
    
    def test_add_drink(self):
        self.assertEqual(4, len(self.coffee_shop.drinks))

    def test_buy_drink(self):
        dave = Customer("Dave", 50.00, 18, 3)
        dave.buy_drink(self.coffee_shop.select_drink("Mocha"))
        self.coffee_shop.increase_till(self.coffee_shop.select_drink("Mocha"))
        self.assertEqual(502.50, self.coffee_shop.till)
        self.assertEqual(47.50, dave.wallet)
    
    def test_age_check(self):
        marge = Customer("Dave", 50.00, 42, 3)
        bart = Customer("Dave", 50.00, 14, 3)

        self.assertEqual(True, self.coffee_shop.check_age(marge, self.coffee_shop.select_drink("Mocha")))
        self.assertEqual(False, self.coffee_shop.check_age(bart, self.coffee_shop.select_drink("Mocha")))
    
    def test_increase_energy_level(self):
        homer = Customer("Homer", 50.00, 45, 3)
        homer.increase_energy_level(self.coffee_shop.select_drink("Mocha"))

        self.assertEqual(5, homer.energy_level)
    
    def test_energy_level_too_high(self):
        homer = Customer("Homer", 50.00, 45, 11)
        marge = Customer("Homer", 50.00, 42, 8)

        self.assertEqual(True, self.coffee_shop.energy_level_too_high(homer))
        self.assertEqual(False, self.coffee_shop.energy_level_too_high(marge))
    
    def test_decrease_energy_level(self):
        homer = Customer("Homer", 50.00, 45, 6)
        steak = Food("Steak", 15.00, 3)
        homer.decrease_energy_level(steak)

        self.assertEqual(3, homer.energy_level)
    
    def test_stock_value(self):
        self.assertEqual(211.5, self.coffee_shop.stock_value())
