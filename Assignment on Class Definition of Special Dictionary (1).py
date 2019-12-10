#Devon Keen
#CS 100-017
#11/29/18
#Assignment on Class Definition of Special Dictionary

#1

class SpecialDictionary:
    '''it contains entries of key value pairs from a special dictionary'''
    def __init__(self):
        self.definitions = {}

    def define(self, word, definition):
        self.definitions[word] = definition

    def get_definition(self, word):
        if word in self.definitions:
            return self.definitions[word]
        else:
            return None

#2

import special_dictionary
farm_animal = special_dictionary.SpecialDictionary()
farm_animal.define("horse", "an adult equine")
farm_animal.define("bull", " a male bovine")
print(farm_animal.get_definition("cow"))
