#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2018 Spring

#MCQ

#1. a
#2. b
#3. e (answer is 4)
#4. e (answer is abcba)
#5. c
#6. b
#7. c
#8. c
#9. b
#10. b

#11a.
def triangle(t,side):
    t.down()
    for i in range(3):
        t.forward(side)
        t.left(120)
    
#11b.
def umbrella(t,side,rotation,count):
    for i in range(count):
        triangle(t,side)
        t.left(rotation)

#12.
def analyzeAreaCodes(phones):
    d = {}
    for phone in phones:
        if phone[0:3] not in d:
            d[phone[0:3]] = 1
        else:
            d[phone[0:3]] +=1
    return d

#13.
def lineStats(inFile,outFile):
   open_in = open(inFile,"tr")
   open_out = open(outFile,"tw")
   vowelCount = 0
   consonantCount = 0
   for line in open_in:
       for char in line:
           if char in "aeiouAEIOU":
                vowelCount +=1
           elif char.isalpha():
                consonantCount +=1
       open_out.write(str(consonantCount)+ " " + str(vowelCount) + "\n")
   open_in.close()
   open_out.close()
   
