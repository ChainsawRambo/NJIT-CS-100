#Devon Keen
#CS 100-017
#9/21/18
#HW2

#3

#3a. 100!
import math
math.factorial(100)
print("100! =",math.factorial(100))

#3b. the log (base 2) of 1,000,000
math.log2(1000000)
print("the log (base 2) of 1,000,000 =",math.log2(1000000))

#3c. the greatest common denominator of 63 and 49
math.gcd(63,49)
print("the greatest common denominator of 63 and 49 =",math.gcd(63,49))

#1 Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular
#  pentagon, each with side length 100.

import turtle
s = turtle.Screen()
pen = turtle.Turtle()

pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
s.clear()

pen = turtle.Turtle()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
s.clear()

pen = turtle.Turtle()
pen.forward(100)
pen.left(72)
pen.forward(100)
pen.left(72)
pen.forward(100)
pen.left(72)
pen.forward(100)
pen.left(72)
pen.forward(100)
pen.left(72)
s.clear()

#2

pen = turtle.Turtle()
pen.circle(50)
pen.right(90)
pen.up()
pen.forward(50)
pen.down()
pen.left(90)

pen.circle(100)
pen.right(90)
pen.up()
pen.forward(50)
pen.down()
pen.left(90)

pen.circle(150)
pen.right(90)
pen.up()
pen.forward(50)
pen.down()
pen.left(90)

pen.circle(200)
pen.right(90)
pen.up()
pen.forward(50)
pen.down()
pen.left(90)
