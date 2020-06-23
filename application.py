
from car import Car

my_volvo = Car("Volvo", "pickup", 300, 4000)
car_evaluation = my_volvo.evaluateCar()
for x in range(len(car_evaluation)):
    print(car_evaluation[x])
