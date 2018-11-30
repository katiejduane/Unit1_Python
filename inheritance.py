# Inheritance!

class Car(object):
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
    def startCar(self):
            print "%s goes vroom!" % self.make

myCar = Car('Ford', 'Fpics', 40)
myCar.startCar()

class Electric_Car(Car):
    # call this object's constructors
    def __init__(self, make, model, battery):
        # call Super class constructor
        super(Electric_Car, self).__init__(make, model, None) # could also say Car().__init__(make, model. "N/A")
        self.battery = battery
    # we can override a parent/super method
    def startCar(self):
        print "%s goes pssshhhhhhh!" % self.make

car1 = Car("Toyota", "Camry", 35)
car2 = Electric_Car("Tesla", "S", "100kh")

print car1.model
car2.startCar()