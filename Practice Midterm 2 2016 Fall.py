#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2016 Fall

#MCQ

#1. a
#2. c
#3. d
#4. d
#5. e (answer is of)
#6. a
#7. b
#8. e (answer is beet)
#9. c
#10. d

#11a.

def letterX(t,length):
    t.down()
    t.right(45)
    t.forward(length/2)
    t.backward(length)
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.backward(length)
    t.forward(length/2)
    t.right(45)

#11b.

def exes(t,initSize,deltaSize,separation,xNum):
    for i in range(xNum):
        letterX(t,initSize)
        t.up()
        t.forward(separation)
        t.down()
        initSize*=deltaSize
        
#12.

def wordLengths(text):
    d = {}
    for word in text.split():
        if len(word) not in d:
            d[len(word)] = 1
        else:
            d[len(word)] +=1
    return d

#13.
def initVowelCount(inFile,outFile):
    r = open(inFile,"tr")
    w = open(outFile,"tw")
    for line in r:
        count = 0
        words = line.split()
        for word in words:
             if word[0] in "aeiouAEIOU":
                 count +=1
        if line == "\n":
             w.write(str(count) + "\n")
    r.close()
    w.close()
             


