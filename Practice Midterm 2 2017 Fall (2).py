#Devon Keen
##CS 100-017
#10/29/18
#Practice Midterm 2 2017 Fall

#MCQ

#1. c
#2. e (answer is aha)
#3. c
#4. a
#5. c
#6. e (answer is 4)
#7. d
#8. b
#9. e (answer is 7)
#10. a

#11a.
def hemispheres(t,radius):
    t.down()
    t.circle(radius)
    t.left(90)
    t.forward(radius*2)
    t.right(180)
    t.forward(radius*2)
    t.left(90)

#11b.
def multispheres(t,size,ratio,angle,num):
    for i in range(num):
        hemispheres(t,size)
        t.left(angle)
        size*=ratio

#12.
def countVowels(text):
    d ={}
    wordList = text.split()
    for word in wordList:
        if word not in d or word in d:
            d[word] = 0
        for letter in word:
            if letter in "aeiouAEIOU":
                d[word] +=1
    return d

#13.
def longestOnLine(inFile,outFile):
    open_inFile = open(inFile,"tr")
    open_outFile = open(outFile, "tw")
    wordCount = 0
    for line in open_inFile:
        wordList = line.split()
        if wordList == []:
            open_outFile.write("\n")
        else:
            for word in wordList:
                if len(word) > wordCount:
                    wordCount = len(word)
            open_outFile.write(str(wordCount))
        open_out.write("\n")
    open_inFile.close()
    open_outFile.close()
