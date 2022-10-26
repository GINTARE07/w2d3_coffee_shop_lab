class Customer:

    def __init__(self, name, wallet, age, energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level
    
    def buy_drink(self, drink):
        self.wallet -= drink.price
    
    def increase_energy_level(self, drink):
        self.energy_level += drink.caffeine_level
    
    def decrease_energy_level(self, food):
        self.energy_level -= food.rejuvenation_level