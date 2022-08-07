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

# creating first car
car1 = Car("Jeep", "Black", "LA875JK", 7905, "AO65706")
print(car1.brand_name)
print(car1.colour)
print(car1.dash_board)