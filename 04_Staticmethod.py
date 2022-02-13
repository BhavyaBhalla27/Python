number = int(input("Enter the number: "))
square = (number)**2
cube = (number)**3
squareroot = (number)**0.5

class Greet:
    @staticmethod
    def greet():
        print("Hello")


class Calculator:
    def __init__(self, square, cube, squareroot):
        self.square = square
        self.cube = cube
        self.squareroot = squareroot
        print(f"The square of the number is {self.square}.\nThe cube of the number is {self.cube}.\nThe square root of the number is {self.squareroot}")


number = Greet()
number.greet()
number = Calculator(square,cube,squareroot)
