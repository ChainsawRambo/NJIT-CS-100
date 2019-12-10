#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2015 Fall

#MCQ

#1. a
#2. b
#3. b
#4. d
#5. d
#6. c
#7. d
#8. e (answer is 0)
#9. b
#10. e (answer is 0)

#11a.

def cup(t,sideLength):
    t.down()
    for i in range(4):
        t.down()
        if i != 3:
            t.forward(sideLength)
        else:
            t.up()
            t.forward(sideLength)
        t.left(90)
        
#11b.
def cups(t,initial,incr,reps):
    for i in range(reps):
        cup(t,initial)
        initial+=incr
        t.right(90)
        t.up()
        t.forward(incr/2)
        t.left(90)
        t.down()
        
#12.

def uniqueWords(inFile,outFile):
    r = open(inFile,"tr")
    w = open(outFile,"tw")
    for line in r:
        wordList = r.split()
        count = 0
        myList = []
        for word in wordList:
            if word not in myList:
                myList.append[word]
                count += 1
        w.write(str(count) + "\n")
    r.close()
    w.close()

#13.

def importantWords(s,threshold):
    d = {}
    for word in s.split():
        if len(word) >= threshold and word not in d:
            d[word] = 0
        if len(word) >= threshold and word in d:
            d[word] += 1
           
    return d
