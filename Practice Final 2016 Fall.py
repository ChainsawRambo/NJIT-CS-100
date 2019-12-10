#Devon Keen
##CS 100-017
#11/29/18
#Practice Final 2016 Fall

#MCQ

#1. b
#2. c
#3. e (5)
#4. a
#5. d
#6. a
#7. a
#8. b
#9. e (4 sided square)
#10. e (9)

#11a. (Told not to do, but already worked on it already)

def regularPoly(t,sideLen,numSides):
    for i in range(numSides):
        t.down()
        t.forward(sideLen)
        t.left(?)

#11b. (Told not to do, but already worked on it already)

import turtle
s = turtle.Screen()
t = turtle.Turtle()
regularPoly(t,100,3)
regularPoly(t,100,4)
regularPoly(t,100,5)
regularPoly(t,100,6)
regularPoly(t,100,7)
regularPoly(t,100,8)


#12.

def wordLengths(inFile,outFile):
    r = open(inFile, "rt")
    w = open(outFile, "wt")
    for line in r:
        words = line.split()
        if len(words) != 0:
            lenLst = []
            for word in words:
                lenLst.append(len(word))
            longest = max(lenLst)
            frequency = lenLst.count(longest)
            w.write(str(longest) + " " + str(frequency))
        w.write("\n")
    r.close()
    w.close()

#13a.

def countVowels(s):
    count = 0
    for letter in s:
        if letter in "aeiouAEIOU":
            count += 1
    return count

#13b.

def vowelFrequency(t):
    lower = t.lower()
    words = lower.split()
    d = {}
    for word in words:
        num = countVowels(word)
        if num not in d:
            d[num] = [word]
        elif word not in d[num]:
            d[num].append(word)
    return d
