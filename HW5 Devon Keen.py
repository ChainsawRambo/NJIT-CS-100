#Devon Keen
#CS 100-017
#10/2/18
#HW5

#1a.
def hasFinalLetter (strList,letters):
    returnList = []
    for string in strList:
        if string[-1] == letters:
            returnList.append(string)
    return returnList

#1b.
sList1 = []
letter1 = "e"
result1 = hasFinalLetter(sList1,letter1)
print(result1)

sList2 = ["Done","do","dove","Dover"]
letter1 = "e"
result2 = hasFinalLetter(sList2,letter1)
print(result2)

sList3 = ["Donkey","do it Mike","Love","Hello World"]
letter1 = "e"
result3 = hasFinalLetter(sList3,letter1)
print(result3)

#2a.
def isDivisible (maxInt,twoInts):
    returnList2 = []
    for num in range(0,maxInt):
        if num % twoInts[0] == 0 and num % twoInts[1] == 0:
            returnList2.append(num)
    return returnList2

#2b
maxInt1 = 0
twoInts1 = (2,5)
answer1 = isDivisible(maxInt1,twoInts1)
print(answer1)

maxInt2 = 20
twoInts2 = (5,10)
answer2 = isDivisible(maxInt2,twoInts2)
print(answer2)

maxInt3 = 100
twoInts1 = (2,5)
answer3 = isDivisible(maxInt3,twoInts1)
print(answer3)
