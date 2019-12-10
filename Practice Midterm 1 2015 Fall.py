#Devon Keen
##CS 100-017
#10/11/18
#Practice Midterm 1 2015 Fall

#MCQ

#1. a
#2. c
#3. d
#4. c
#5. b
#6. c
#7. a
#8. c
#9. a
#10. e. answer is Error

#11a.
def equalSign(t,length):
    t.down()
    t.forward(length)
    t.backward(length)
    t.up()
    t.right(90)
    t.forward(length/2)
    t.left(90)
    t.down()
    t.forward(length)
    t.backward(length)
    t.left(90)
    t.up()
    t.forward(length/2)
    t.down()
    t.right(90)
    
#11b.
def equalSigns(t,size,spacing,num):
    for i in range(num):
        equalSign(t,size)
        t.up()
        t.forward(size+spacing)
        turt.down()

#12.
def vowelCount(text):
    start=0
    for string in text:
        if string in "AEIOUaeiou":
            start+=1
    return start

#13.
def getInitials(remark):
    returnList =[]
    name1 = input("What is your first name?")
    name2 = input("What is your last name?")
    print(remark,name1,name2)
    return name1[0]+name2[0]
