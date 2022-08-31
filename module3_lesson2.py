from operator import truediv


class Car:
    tire = 4
    door = 4
    bumper = 2
    wind_screen = True
    dash_board = True
    def __init__(self, brand_name, colour, plate_number, mileage, chasis_no):
        self.brand_name = brand_name
        self.colour = colour
        self.plate_number = plate_number
        self.mileage = mileage
        self.chasis_no = chasis_no

    def car_name(self):
        print(self.brand_name)

    def car_colour(self):
        print(self.colour)

    def plate_no(self):
        print(self.plate_number)

    def car_mileage(self):
        print (self.mileage)

    def chasis(self):
        print(self.chasis_no)


# creating car instances
car1 = Car("Jeep", "Black", "LA875JK", 7905, "AO65706")

car2 = Car("Toyota", "Red", "FR676GH", 5777, "GF66690")

car1.car_name()
car1.car_mileage()
car2.car_name()
car2.car_colour()
