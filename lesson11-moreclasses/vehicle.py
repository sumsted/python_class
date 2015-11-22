class Vehicle:
    def __init__(self, wheels, color, speed):
        self.color = color
        self.wheels = wheels
        self.speed = speed

    def __gt__(self, other):
        if self.speed > other.speed:
            return True
        else:
            return False

    def how_fast(self):
        if self.speed < 30:
            return 'slow'
        elif self.speed >= 30:
            return 'fast'


class Bike(Vehicle):
    def __init__(self, name, color, basket):
        super().__init__(2, color, 20)
        self.name = name
        self.basket = basket

    def description(self):
        return "%s's %s %s %s" % (self.name, self.how_fast(), self.color, type(self).__name__.lower())


class Car(Vehicle):
    def __init__(self, name, color, engine, doors):
        super().__init__(4, color, 60)
        self.name = name
        self.engine = engine
        self.doors = doors

    def description(self):
        return "%s's %s %s %s" % (self.name, self.how_fast(), self.color, type(self).__name__.lower())

# create a new class called skateboard

if __name__ == '__main__':
    bike = Bike('Matt', 'blue', True)
    car = Car('John', 'red', 4, 4)
    print(bike.description())
    print(bike.how_fast())

    print(car.description())
    print(car.how_fast())

    if car > bike:
        print(car.description(), 'is faster than', bike.description())
    else:
        print(bike.description(), 'is faster than', car.description())

    # which is faster a skateboard or bike
