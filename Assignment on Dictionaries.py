#Devon Keen
#CS 100-017
#10/25/18
#Assignment on Dictionaries

#1
def initialLetterCount(wordList):
    d = {}
    for word in wordList:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d
horton = ['I','say','what','I','mean','and','I','mean','what','I','say']
print(initialLetterCount(horton))

#2
def initialLetter(wordList):
    d = {}
    for word in wordList:
        if word[0] not in d:
            d[word[0]] = [word]
            
    return d
print(initialLetter(horton))

#3
def shareALetter(wordList):
    d = {}
    for word in wordList:
        if word not in d:
            d[word] = [word]
            for letter in word:
                for word2 in wordList:
                    if letter in word2 and word2 not in d[word]:
                        d[word].append(word2)
                      
    return d
print(shareALetter(horton))

