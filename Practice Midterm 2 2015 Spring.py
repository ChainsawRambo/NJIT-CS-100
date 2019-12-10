#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2015 Spring

#MCQ

#1. c
#2. c
#3. a
#4. d
#5. d
#6. e (answer is ['', ['Ebola', 'SARS']] )
#7. d
#8. c
#9. e (answer is [2, 3, 3, 1, 4] )
#10. b

#11a.

def halfSquare(t,length):
    for i in range(2):
        t.down()
        t.forward(length)
        t.left(90)
        
#11b.

def halfSquares(t,initial,increment,reps):
    for i in range(reps):
        halfSquare(t,initial)
        initial+=increment

#12.

def wordCount(inFile,outFile):
    r = open(inFile,"tr")
    w = open(outFile,"tw")
    for line in r:
        wordList = line.split()
        count = len(wordList)
        w.write(str(count) + "\n")
    r.close()
    w.close()

#13.

def initialVowels(inFile):
    d ={}
    r = open(inFile)
    lineList1 = r.lower()
    lineList2 = lineList1.split()
    for line in lineList2:
        for word in line:
            if word[0] in "aeiou" and word not in d:
                d[word[0]] = [word]
            elif word[0] in "aeiou" and word in d:
                d[word[0]].append[word]
    return d
    
        
