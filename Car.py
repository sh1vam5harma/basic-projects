class Car: #CREATE CLASS OBJECT, IT IS SUBJECTIVE

    def __init__(self, speed=0): #DEFINE FIRST FNCTN USING INSTANTIATE
        self.speed = speed #ARGUMENT
        self.odometer = 0 #ARGUMENT
        self.time = 0 #ARGUMENT

    def say_state(self): #DEFINE SECOND FNCTN
        print("I'm going {} kph!".format(self.speed)) #FORMAT THE PRINT STRING

    def accelerate(self): #DEFINE THIRD FUNCTION
        self.speed += 5 #ADDS 5 TO VALUE & ASSIGNS NEW VALUE

    def brake(self): #DEFINE FOURTH FUNCTION
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5 #SUBTRACT 5 FROM VALUE AND ASSIGN NEW VALUE

    def step(self): #DEFINE FIFTH FUNCTION FOR ODOMETER READING
        self.odometer += self.speed
        self.time += 1

    def average_speed(self): #DEFINE SIXTH FUNCTION FOR AVG SPEED
        if self.time != 0: #IF NOT EQUAL ZERO
            return self.odometer / self.time
        else:
            pass #DO NOTHING


if __name__ == '__main__': #SPECIAL VARIABLE

    my_car = Car()
    print("I'm a car!")
    while True: #RUNS INFINITELY UNTIL STOPPED
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper() #CAPITALIZES
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
