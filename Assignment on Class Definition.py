#Devon Keen
##CS 100-017
#11/13/18
#Assignment on Class Definition

#1
class Dog:
    '''Tells you what kind of dog it is'''
    species = 'Canis familiaris'
    def __init__(self,name,breed):
        self.sName = name
        self.sBreed = breed
        self.tricks = []
        
    def teach(self,trickName):
        if trickName not in self.tricks:
            self.tricks.append(trickName)
            print("Yes,",self.sName,"knows",trickName)
            
    def knows(self,trickName):
        if trickName in self.tricks:
            return True
        else:
            print("No,",self.sName,"doesn't know",trickName)
            return False
            
import dog
sugar = dog.Dog('Sugar', 'border collie')
print(sugar.sName)
print(sugar.sBreed)

#2
print(sugar.tricks)

#3
print(sugar.teach('frisbee'))

#4
print(sugar.knows('frisbee'))
print(sugar.knows('arithmetic'))

#5
print(dog.Dog.species)
print(sugar.species)


