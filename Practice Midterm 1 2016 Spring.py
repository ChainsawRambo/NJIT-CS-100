#Devon Keen
##CS 100-017
#10/11/18
#Practice Midterm 1 2016 Spring

#MCQ

#1. e answer is 2 and 3
#2. b
#3. c
#4. b
#5. c
#6. a
#7. c
#8. a
#9. b
#10. e answer is ott

def rangeExample(aString, stop, interval):
    returnVal = ''
    myRange = range(1, stop, interval)
    for idx in myRange:
        returnVal += aString[idx]
    return returnVal
print(rangeExample('Do unto others', 13, 4))

#11a.
def drawSquare(t,length):
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    
#11b.
def drawSquares(t,size,num,angle):
    for i in range(num):
        drawSquare(t,size)
        t.right(angle)

#12.
def bigCount(numList,threshold):
    start=0
    for string in numList:
        if string >= threshold:
            start+=1
    return start

#13.
def getDate(message):
    returnList =[]
    month = input("What month is it?")
    day = input("What day is it?")
    print(month,day,message)
    return month+" "+day
