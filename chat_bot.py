import random
from datetime import datetime

class ChatBot:

    base_greetings = ['Hi', 'Hello', 'Greetings']
    timefactored_greetings = dict(Morning = "Isn't it a nice morning!", Evening = "Lovely evening, isn't it?", Midday = "Happy midday by the way.", Night = "You should go to sleep maybe?")
    annoying_greeting = ['Fuck you!', 'You suck!']

    def __init__(self, annoyance_level):
        self.annoyance_level = annoyance_level

    def greetChatter(self):
        if self.annoyance_level >= 75:
            i = random.randrange(0, len(self.timefactored_greetings), 1)
            print(self.annoying_greeting[i])
        else:
            i = random.randrange(0, len(self.base_greetings), 1)
            print(self.base_greetings[i])
            self.timeGreeting()


    def timeGreeting(self):
        now = datetime.now()
        current_time = now.hour
        if (current_time >= 0 and current_time <=5):
            print(self.timefactored_greetings['Night'])
        elif (current_time >= 5 and current_time <= 10):
            print(self.timefactored_greetings['Morning'])
        elif (current_time >= 10 and current_time <= 17):
            print(self.timefactored_greetings['Midday'])
        else:
            print(self.timefactored_greetings['Evening'])
