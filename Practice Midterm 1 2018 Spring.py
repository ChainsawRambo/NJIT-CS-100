#Devon Keen
##CS 100-017
#10/9/18
#Practice Midterm 1 2018 Spring

#MCQ

#1. c
#2. c
#3. e
#4. d
#5. e
#6. b
#7. c
#8. b
#9. a
#10. d

#11a.
def stair(t,tread_size,riser_height):
    t.down()
    t.forward(tread_size)
    t.right(90)
    t.forward(riser_height):
    t.left(90)
    
#11b.
def staircase(turt,num_stairs,tread_size,riser_height):
    for i in range(num_stairs):
        stair(turt,tread_size,riser_height)

#12.
def vowel_tracker(words):
    start = 0
    end = 0
    for string in words:
        if string[0] in "AEIOUaeiou":
            start+=1
        if string[-1] in "AEIOUaeiou":
            end+=1
    return[start,end]

#13.
def month_info(medium_length):
    month = input("What month is it?")
    days = int(input("How many days is in",month,"?"))
    if days > medium_length:
        print(month,"is long")
    elif days < medium_length:
        print(month,"is short")
    else:
        print(month,"is medium")
    return month
