#Devon Keen
#CS 100-017
#10/18/18
#Assignment on While Loops

#1
def twoWords(length,firstLetter):
    while True:
        word1 = input("Enter a word that is the length of variable length please")
        if len(word1)==length:
            word2 = input("Enter a word beginning with the letter of variable firstLetter please")
            if word2[0] == firstLetter:
                return [word1,word2]
            elif word2[0]==firstLetter.lower():
                return [word1,word2]
        else:
            break

#2
def twoWordsV2(length,firstLetter):
    while not False:
        word1 = input("Enter a word that is the length of variable length please")
        if len(word1)==length:
            word2 = input("Enter a word beginning with the letter of variable firstLetter please")
            if word2[0] == firstLetter:
                return [word1,word2]
            elif word2[0] == firstLetter.lower():
                return [word1,word2]

#3
def enterNewPassword():
    containDigit = False
    passcode = False
    char = 0
    while passcode == False:
        password = input("Enter a password that has 8-15 characters, including at least one digit")
        if len(password)>=8 and len(password)<=15:
            print("Password is between 8-15 characters")
            passcode = True
        else:
            print("Password is either too short or too long")
        while char < len(password):
            if password[char] in "0123456789":
                containDigit = True
                break
            else:
                char+=1
    if containDigit == True:
        print("Password contains at least one digit")
        passcode = True
    else:
        print("Your password does not contain any digit")

#4
import random
answer = random.randint(0,50)
count = 0
while count != 5:
    number = int(input("I'm thinking of a number in the range 0-50.  You have five tries to guess it."))
    if number == answer:
                print("You are right! I was thinking of 24!")
                break
    if number > answer:
                print(number,"is too high")
                count+=1
    if number < answer:
                print(number,"is too low")
                count+=1
    if count==5:
                print(answer,"was the correct answer")

            
       
    
