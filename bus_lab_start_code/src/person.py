class Person:
    def __init__(self, name, age, cash, destination):
        self.name = name
        self.age = age
        self.cash = cash
        self.destination = destination

    def pay_fare(self, bus):
        self.cash -= bus.price
        bus.total_cash += bus.price
