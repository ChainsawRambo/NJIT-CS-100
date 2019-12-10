#Devon Keen
#CS 100-017
#10/25/18
#Assignment on Files

#1
def file_copy(in_file,out_file):
    open_out = open(out_file,"tw")
    open_in = open(in_file,"tr")
    for word in open_in:
        open_out.write(word)
    open_in.close()
    open_out.close()
    
#2
def file_stats(in_file):
    open_in = open(in_file,"tr")
    read_in = open_in.read()
    print(len(read_in.split()),"words", end = "\n")
    print(read_in.count("\n"),"lines", end = "\n")
    print(len(read_in),"characters", end = "\n")
    open_in.close()

file_stats("created_equal.txt")

#3
import string
def repeat_words(inputFile,outputFile):
    open_inputFile = open(inputFile,"tr")
    open_outputFile = open(outputFile,"tw")
    lines = open_inputFile.readlines()
    for line in lines:
        words = []
        duplicates = []
        for word in line.split():
            p = string.punctuation
            word = word.lower().strip(p)
            if word not in words:
                words.append(word)
            elif word in words and word not in duplicates:
                duplicates.append(word)
        for word in duplicates:
            open_outputFile.write(word + " ")
        open_outputFile.write("\n")
            
    open_inputFile.close()
    open_outputFile.close()

inF = "catInTheHat.txt"
outF = "catRepWords.txt"
repeat_words(inF,outF)
