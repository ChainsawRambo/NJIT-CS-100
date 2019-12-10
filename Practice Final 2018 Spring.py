#Devon Keen
##CS 100-017
#11/20/18
#Practice Final 2018 Spring

#MCQ

#1. c
#2. b
#3. e (e)
#4. a
#5. d
#6. e (bbob)
#7. d
#8. c
#9. e (1)
#10. a

#11a.

class Section:
    '''it describes a section of a course'''
    def __init__(self,section_id):
        self.section_id = section_id
        self.enrolled_students = []
    def enroll(self,studentname):
        if studentname not in self.enrolled_student:
            self.enrolled_students.append(studentname)
    def is_enrolled(self,name):
        if name in self.enrolled_students:
            return True
        else:
            return False

#11b.

import section
s1 = section.Section("Math111_101")
s1.enroll("Joe Josephson")
s1.enroll("Mary Smith")
print(s1.is_enrolled("Mary Josephson"))

#12.

def inverse(diction):
    d = {}
    for student_key in diction:
        courseList = diction[student_key]
        for course in courseList:
            if course not in d:
                d[course] = [student_key]
            else:
                d[course].append(student_key)
    return d

#13.

def fileStats(inFile,outFile):
    r = open(inFile, "rt")
    w = open(outFile, "wt")
    for line in r:
        wordList = line.split()
        words = len(wordList)
        count = 0
        for word in wordList:
            for char in word:
                if char.isdigit():
                    count += 1
        w.write(str(words) + " " + str(count) + "\n")
    r.close()
    w.close()

