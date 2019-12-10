#Devon Keen
##CS 100-017
#11/20/18
#Practice Final 2017 Fall

#MCQ

#1. b
#2. c
#3. d
#4. e (f)
#5. d
#6. b
#7. e (never ending loop)
#8. d
#9. e (Key Error)
#10. a

#11a.

class State:
    '''it describes a state'''
    def __init__(self,name):
        self.name = name
        self.universities = []
    def addUniversity(self,uName):
        if uName not in self.universities:
            self.universities.append(uName)
    def is_home_of(self,uName):
        if uName in self.universities:
            return True
        else:
            return False

#11b.

import state
s1 = state.State("New Jersey")
s1.addUniversity("NJIT")
s1.addUniversity("Princeton")
print(s1.is_home_of("MIT"))

#12.

def wordLineCount(inFile):
    d = {}
    r = open(inFile,"rt")
    wordList = r.split()
    for word in wordList:
        if word not in d:
            d[word] = 0
    for line in r:
        wordList2 = line.split()
        for word in wordList2:
            if word in d:
                d[word] += 1
    return d

#13.

def lineStats(inFile,outFile, threshold):
    r = open(inFile, "rt")
    w = open(outFile, "wt")
    for line in r:
        lower = line.lower()
        wordList = lower.split()
        words = len(wordList)
        count = 0
        duplicates = []
        for word in wordList:
            if len(word) > threshold and word not in duplicates:
                    count += 1
                    duplicates.append(word)
        w.write(str(words) + " " + str(count) + "\n")
    r.close()
    w.close()
