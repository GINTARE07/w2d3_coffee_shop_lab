class CoffeeShop:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
    
    def increase_till(self, drink):
        self.till += drink.price
    
    def new_drink(self, drink, stock):
        self.drinks.append({"info": drink, "stock": stock})
    
    def select_drink(self, drink_name):
        for drink in self.drinks:
            if drink["info"].name == drink_name:
                return drink["info"]
    
    def check_age(self, customer, drink):
        if customer.age <= 16 and drink.caffeine_level == 0:
            return True
        elif customer.age >= 16:
            return True
        else:
            return False

    def energy_level_too_high(self, customer):
        return customer.energy_level > 10

    def stock_value(self):
        stock_value = 0
        for drink in self.drinks:
            drink_price = drink["info"].price
            drink_stock = drink["stock"]
            stock_value += (drink_price * drink_stock)
        
        return stock_value

