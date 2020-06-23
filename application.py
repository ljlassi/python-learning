
from car import Car

car_manufacturer = input("Your car manufacturer? \n")
car_type = input("Your car type? e.g. Pickup? \n")
car_max_speed = int(input("Your car's max speed? \n"))
car_weight = int(input("Your car's weight? \n"))

my_car = Car(car_manufacturer, car_type, car_max_speed, car_weight)
car_evaluation = my_car.evaluateCar()
for x in range(len(car_evaluation)):
    print(car_evaluation[x])
