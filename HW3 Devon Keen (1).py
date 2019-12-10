#Devon Keen
#CS 100-017
#9/25/18
#HW3

#1-2
a = 3
b = 4
c = 5

if a < b:
    print("OK,a < b ")
else:
    print("NOT OK")
if c < b:
    print("OK,c < b ")
else:
    print("NOT OK,c is not < b")
if a+b==c:
    print("OK, a+b==c")
else:
    print("NOT OK,a+b==c")
if a**2 + b**2 == c**2:
    print("OK, a**2 + b**2 == c**2")
else:
    print("NOT OK")

#3

color = input("Enter color")
width = int(input("Enter width"))
lineLength = int(input("Enter line length"))
shape = input("Enter shape of a line, triangle, or square")

import turtle
s = turtle.Screen()
pen = turtle.Turtle()


pen.color(color)
pen.width(width)
if shape == "line":
        pen.forward(lineLength)
if shape == "triangle":
        pen.forward(lineLength)
        pen.right(120)
        pen.forward(lineLength)
        pen.right(120)
        pen.forward(lineLength)
        pen.right(120)
if shape == "square":
        pen.forward(lineLength)
        pen.right(90)
        pen.forward(lineLength)
        pen.right(90)
        pen.forward(lineLength)
        pen.right(90)
        pen.forward(lineLength)
        pen.right(90)
