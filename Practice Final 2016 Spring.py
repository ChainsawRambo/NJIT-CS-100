#Devon Keen
##CS 100-017
#12/4/18
#Practice Final 2016 Spring

#MCQ

#1. b
#2. a
#3. e (1)
#4. a
#5. c
#6. a
#7. b
#8. c
#9. c
#10. d

#11a. (Told not to do, but already worked on it already)

def midline(t,length):
    for i in range(2):
        t.down()
        t.forward(length)
        t.left(90)

#11b. (Told not to do, but already worked on it already)

def halfSquares(t,increment,num):
    for i in range(num):
        halfSqaure(t,increment)

#12.

def mostFrequent(inFile,outFile):
    r = open(inFile, "rt")
    w = open(outFile, "wt")
    for line in r:
        d = {}
        for char in line:
            if char != " ":
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
        mostFreq = max(d.values())
        mostFreqChars = ""
        for key in d:
            if d[key] == mostFreq:
                mostFreqChars += key
        w.write(mostFreqChars + "\n")
    r.close()
    w.close()

#13a.

def longEnough(s,threshold):
    if len(s) >= threshold:
        return True
    else:
        return False

#13b.

def longWords(t,i):
    words = t.split()
    d = {}
    for word in words:
        if longEnough(word,i) == True and word not in d:
            d[word] = word.count(t)
    return d
