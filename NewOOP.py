
class Car:
    x = 1

    def drive(self):
        print("driving the car")

a = "A"
polo = Car()
mini = Car()

Car.drive(polo)
Car.drive(mini)

polo.drive()
mini.drive()

print(type(a))
print(type(polo))
