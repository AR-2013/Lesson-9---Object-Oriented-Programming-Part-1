class robot:

    species = "robot"

    def __init__(self, name, age):
        self.name = name
        self.age = age
mia = robot("Mia", 12)

print("{} is a {} and she is {} years old".format(mia.name, mia.species, mia.age ))