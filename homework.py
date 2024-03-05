class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Blender(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def blend(self):
        print(f"Перемалывание {self.brand} {self.model}со скоростью {self.speed}.")

class MeatGrinder(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def grind(self):
        print(f"Измельчение мяса  {self.brand} {self.model} с емкостью {self.capacity}.")



class Ship:
    def __init__(self, name, length, crew):
        self.name = name
        self.length = length
        self.crew = crew

class Frigate(Ship):
    def __init__(self, name, length, crew, guns):
        super().__init__(name, length, crew)
        self.guns = guns

    def fire(self):
        print(f"Firing {self.guns} guns from {self.name}.")

class Destroyer(Ship):
    def __init__(self, name, length, crew, missiles):
        super().__init__(name, length, crew)
        self.missiles = missiles

    def launch_missiles(self):
        print(f"Launching {self.missiles} missiles from {self.name}.")

class Cruiser(Ship):
    def __init__(self, name, length, crew, torpedoes):
        super().__init__(name, length, crew)
        self.torpedoes = torpedoes

    def launch_torpedoes(self):
        print(f"Launching {self.torpedoes} torpedoes from {self.name}.")      




class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars = dollars
        self.cents = cents

    def set_money(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display_money(self):
        print(f"Money: ${self.dollars}.{self.cents}")          