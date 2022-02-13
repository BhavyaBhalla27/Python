class Animals:
    animalType = "Reptile"
class Pet(Animals):
    color = "Black"
class Dog(Pet):
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()
print(d.animalType)
print(d.color)