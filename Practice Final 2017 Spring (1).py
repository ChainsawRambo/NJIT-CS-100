#Devon Keen
##CS 100-017
#11/27/18
#Practice Final 2017 Spring

#MCQ

#1. e (4)
#2. b
#3. e (Key Error)
#4. d
#5. b
#6. b
#7. d
#8. e (5)
#9. e (1)
#10. a

#11a. (Told not to do, but worked on some of it already)

def halfSquare(t,length):
    for i in range(2):
        t.down()
        t.forward(length)
        t.left(90)

#11b. (Told not to do, but worked on some of it already)

def halfSquares(t,increment,num):
    for i in range(num):
        halfSquare(t,increment)

#12.

def lineStats(inFile,outFile):
    r = open(inFile,"rt")
    w = open(outFile, "wt")
    for line in r:
        lower = line.lower()
        words = lower.split()
        uwords = []
        chars = []
        for word in words:
            if word not in uwords:
                uwords.append(word)
        for char in line[:-1]:
            if char not in chars:
                chars.append(char)
        w.write("words" + str(len(uwords)) + "chars" + str(len(chars)) + "\n")
    r.close()
    w.close()

#13.

def vowelEndings(text):
    d = {}
    words = text.split()
    for word in words:
        if word[-1] in "aeiou":
            if word[-1] not in d:
                d[word[-1]] = [word]
            elif word not in d[word[-1]]:
                d[word[-1]].append(word)
    return d
        

