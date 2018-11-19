# # Objects!
# # A CLASS is a recipe, an OBJECT is the food you made with the recipe. It can be reused over and over!

# # Our blueprint for making cars. 
# class Car(object):
#     # Whenever we start making a new car (or any object) we run __init__ and pass (self) as the first arg!
#     def __init__(self):
#         # Self is special. It refers to THIS object.
#         self.make = "Honda"
#         self.model = "Accord"
#         self.year = 2007

# myCar = Car() # THIS is where it becomes an object, made from the car class above
# print myCar.make, myCar.model

# yourCar = Car() # This is also an object
# yourCar.make = "Toyota" # You can change the data within your object, but it doesn't change the original class (Car, in this case)
# print yourCar.make

class Car(object):
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def change_model(self, newModel):
        self.model = newModel

zacsCar = Car('Ford', 'Escort', 2003, 'Silver')

crisCar = Car('Chevrolet', 'Malibu', 2008, 'Black')
crisCar.fuel = "Gas"
print zacsCar.make, zacsCar.color
print crisCar.fuel

zacsCar.change_model("Fiesta")
print zacsCar.model

