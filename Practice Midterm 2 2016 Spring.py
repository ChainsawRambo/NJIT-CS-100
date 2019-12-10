#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2016 Spring

#MCQ

#1. a
#2. d
#3. c
#4. d
#5. e (nothing happens when you run it, only an empty line)
#6. e (Key Error)
#7. c
#8. d
#9. d
#10. e (answer is 4)

#11a.

def capitalL(t,width):
    height = 2*width
    t.down()
    t.forward(width)
    t.backward(width)
    t.left(90)
    t.forward(height)
    t.backward(height)
    t.right(90)

#11b.

def Ls(t,initWidth,multiplier,reps,angle):
    for i in range(reps):
        capitalL(t,initWidth)
        initWidth*=multiplier
        t.right(angle)

#12.

def initialDict(text):
    d ={}
    wordList = text.split()
    for word in wordList:
        if word[0] not in d:
            d[word[0].lower()] = [word]
        else:
            d[word[0].lower()].append(word)
    return d

#13.

def lineStats(infile,outfile):
    r = open(infile,"tr")
    w = open(outFile,"tw")
    wordCount = 0
    charCount = 0
    for line in r:
        wordList = line.split()
        for word in wordList:
            wordCount +=1
            for char in word:
                charCount +=1
    w.write(str(wordCount) + " " + str(charCount) + "\n")
    r.close()
    w.close()
        
    


