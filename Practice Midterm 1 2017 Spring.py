#Devon Keen
##CS 100-017
#10/9/18
#Practice Midterm 1 2017 Spring

#MCQ

#1. d
#2. d
#3. e, [3] is the result
#4. a
#5. b (technically 3 sides of a rectangle)
#6. d
#7. b
#8. b
#9. a
#10. d

#11a.
def midline(t,lineLength):
    t.down()
    t.backward(lineLength/2)
    t.forward(lineLength)
    t.backward(lineLength/2)

#11b.
def spiral(t,length,multiplier,numlines,angle):
    for i in range(numlines):
        midline(t,length)
        t.left(angle)
        length*=multiplier

#12.
def evenLengths(stringList):
    returnList =[]
    for string in stringList:
        if len(string) % 2 == 0:
            returnList.append(string)
    return returnList

#13.
def courseLoad(light,heavy):
    returnList = []
    courseCredits = int(input("How many credits are you taking?"))
    if courseCredits <= light:
        print(courseCredits," is a light schedule")
        return "light"
    if courseCredits >= heavy:
        print(courseCredits," is a heavy schedule")
        return "heavy"
    else:
        print(courseCredits," is an average schedule")
        return "average"




 
        
        
    
