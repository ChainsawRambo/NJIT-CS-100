#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2017 Spring

#MCQ

#1. a
#2. b
#3. c
#4. a
#5. d
#6. e (answer is a)
#7. d
#8. b
#9. c
#10. e (answer is 47)

#11a.
def tri(t,length):
    t.down()
    for i in range(3):
        t.forward(length)
        t.backward(length)
        t.left(120)

#11b.
def tris(t,initSize,ratio,rotation,num):
    for i in range(num):
        tri(t,initSize)
        t.left(rotation)
        initSize*=ratio

#12.
def initialLets(t):
    d = {}
    wordList = t.split()
    for word in wordList:
        if word[0] not in d:
            d[word[0]] = 1
        else:
            d[word[0]] += 1
    return d

#13.
def initVowels(inFile,outFile):
    open_inFile = open(inFile,"tr")
    open_outFile = open(outFile,"tw")
    for line in open_inFile:
        wordList = line.split()
        for word in wordList:
            if word[0] in "aeiouAEIOU":
                open_outFile.write(word + " ")
        open_outFile.write("\n")

    open_inFile.close()
    open_outFile.close()
