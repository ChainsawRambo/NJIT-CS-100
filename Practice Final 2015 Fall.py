#Devon Keen
##CS 100-017
#12/6/18
#Practice Final 2015 Fall

#MCQ

#1. a
#2. e (invalid syntax)
#3. e (Type Error)
#4. d
#5. c
#6. a
#7. b
#8. c
#9. e (5)
#10. e (text is not defined)

#11a. (Told not to do, but already worked on it already)

def tri(t,sideLen):
    for i in range(3):
        t.down()
        t.forward(sideLen)
        t.left(120)

#11b. (Told not to do, but already worked on it already)

def tris(t,initial,incr,num,angle):
    for i in range(num):
        tri(t,initial)
        t.left(angle)
        initial += incr

#12.

def wordsByLine(inFile,outFile):
    r = open(inFile, "rt")
    w = open(outFile, "wt")
    for line in r:
        words = line.split()
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        for key in d:
            w.write(key + ":" + str(d[key]) + " ")
        w.write("\n")
    r.close()
    w.close()

#13.

def lineIndex(fName):
    d = {}
    r = open(fName, "rt")
    lines = r.readlines()
    lineNum = 0
    for line in lines:
        wordList = line.split()
        for word in wordList:
            if word not in d:
                d[word] = [lineNum]
            elif lineNum not in d[word]:
                d[word].append(lineNum)
        lineNum += 1
    r.close()
    return d
