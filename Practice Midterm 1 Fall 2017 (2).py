#Devon Keen
##CS 100-017
#10/9/18
#Practice Midterm 1 2017 Fall

#MCQ

#1. a
#2. c
#3. e
#4. d
#5. e
#6. b
#7. a
#8. a
#9. d
#10. d

#11a.
def double_circle(t,radius):
    t.down()
    for i in range(2):
        t.circle(radius)
        t.right(180)
        
#11b.
def circle_line(t,radius,multiplier,num_repeats,separation):
    for i in range (num_repeats):
        double_circle(t,radius)
        t.up()
        t.forward(separation)
        t.down()
        radius*=multiplier
#12.
def partial_symmetry(string_list):
    returnList = []
    for string in string_list:
        if len(string)% 2 == 0 and string[0] == string[-1]:
            returnList.append(string)
        if len(string) % 2 == 1:
            returnList.append(string)
    return returnList
       
#13.
def greet_student(state,in_msg,out_msg):
    returnList = []
    name = input("What is your name?")
    state = input("What is state are you from in capital two-letter abbreviation?")
    if state == "NJ":
        print(in_msg,name)
    else:
        print(out_msg,name)
    return (name,state)




        



