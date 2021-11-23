class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.total_cash = 0
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            if self.capacity < 1:
                return

            if self.destination == passenger.destination:
                self.pick_up(passenger)
                self.capacity -= 1
                bus_stop.queue.remove(passenger)

        # self.passengers.extend(bus_stop.queue)
        # bus_stop.clear()
