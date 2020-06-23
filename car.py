
class Car:

    def __init__(self, manufacturer, type, max_speed, weight):
        self.manufacturer = manufacturer
        self.type = type
        self.max_speed = max_speed
        self.weight = weight

    def evaluateCar(self):
        evaluate_manufacturer = ""
        evaluate_type = ""
        evaluate_max_speed = ""
        evaluate_weight = ""
        if self.manufacturer == "Ford":
            evaluate_manufacturer = "Based on car type - Your car is going to blow up, lol."
        elif self.manufacturer == "Volvo":
            evaluate_manufacturer = "Based on car type - Your car is not going to blow up."
        else:
            evaluate_manufacturer = "Based on car type - Your car is probably not going to blow up."
        if self.type == "pickup":
            evaluate_type = "Pickup - Are you a redneck???!!!"
        else:
            evaluate_type = "I guess you are fine in terms of car type"
        if self.max_speed < 250:
            evaluate_max_speed = "Your car is too slow for you, but maybe that's a good thing."
        else:
            evaluate_max_speed = "Your car goes fast, and is going kill you :o"
        if self.weight < 1000:
            evaluate_max_speed = "In a car crash, your car weight means you are more likely to die than the other party"
        else:
            evaluate_weight = "Don't kill anyone with your carrr!!!!!!"
        return [evaluate_manufacturer, evaluate_type, evaluate_max_speed, evaluate_weight]
