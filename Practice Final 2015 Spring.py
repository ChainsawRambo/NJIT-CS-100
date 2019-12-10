#Devon Keen
##CS 100-017
#12/6/18
#Practice Final 2015 Spring

#MCQ

#1. b
#2. a
#3. a
#4. d
#5. d
#6. e (3)
#7. d
#8. e (True: 3, False: 2)
#9. c
#10. d

#11a. (Told not to do, but already worked on it already)

def capT(turt,height):
    turt.down()
    turt.left(90)
    turt.forward(height)
    turt.right(90)
    turt.forward(height/4)
    turt.backward(height/2)
    turt.forward(height/4)
    turt.right(90)
    turt.forward(height)
    turt.left(90)

#11b. (Told not to do, but already worked on it already)

def tRaw(t,num,init,ratio):
    for i in range(num):
        capT(t,init)
        t.up()
        t.forward(init/2)
        t.down()
        init *= ratio

#12.

import string
def fileStats(inFile,outFile):
    r = open(inFile, "rt")
    w = open(outFile, "wt")
    lines = r.readlines()
    l,words,c,p,d = 0,0,0,0,0
    l = len(lines)
    for line in lines:
        c += len(line)
        wordList = line.split()
        words += len(wordList)
        for char in line:
            if char in string.punctuation:
                p += 1
            if char.isdigit():
                d += 1
    w.write("characters" + " " + str(c) + "\n")
    w.write("words" + " " + str(words) + "\n")
    w.write("lines" + " " + str(l) + "\n")
    w.write("digits" + " " + str(d) + "\n")
    w.write("punctuation" + " " + str(p) + "\n")
    r.close()
    w.close()

#13.

def symmetry(text):
    d = {}
    lower = text.lower()
    words = lower.split()
    for word in words:
        if word[0] == word[-1] and word[0] not in d:
            d[word[0]] = 1
        if word[0] == word[-1] and word[0] in d:
            d[word[0]] += 1
    return d
