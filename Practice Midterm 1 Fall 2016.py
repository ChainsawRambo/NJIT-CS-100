#Devon Keen
##CS 100-017
#10/11/18
#Practice Midterm 1 2016 Fall

#MCQ

#1. e, answer was 17
#2. b
#3. c
#4. e, answer was -2
#5. d
#6. a
#7. d
#8. b
#9. d
#10. c

#11a.
def concentric(t,radius):
    t.down()
    t.circle(radius)
    t.up()
    t.left(90)
    t.forward(radius)
    t.right(90)
    
#11b.
def dartboard(t,numRings,delta):
    radius=delta
    for i in range(numRings):
        t.up()
        t.right(90)
        t.forward(radius)
        t.left(90)
        t.down()
        concentric(t,radius)
        radius = radius + delta

#12.
def strLenParity(stringList):
    start=0
    end=0
    for string in stringList:
        if len(string)%2==0:
            start+=1
        else:
            end+=1
    return[start,end]

#13.
def nameLenComment(short,long):
    returnList =[]
    name = input("What is your name?")
    if len(name) <= short:
        print(name,", your name is short")
    elif len(name) >= long:
        print(name,", your name is long")
    else:
        print(name,", your name is about average length")
    return name
