import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Homer", 50.00, 18, 3)
    
    def test_customer_has_name(self):
        self.assertEqual("Homer", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)
    
    