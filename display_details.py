#Write a Python program to display your details like name, age, address in three different lines.
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print(self):
        print(self.name,"\n", self.age, "\n", self.address )

person = Person("Zeke","25", "Liberio, Marley" )
person.print()
person = Person("Annie","20", "Liberio, Marley" )
person.print()