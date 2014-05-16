#WWSavior is a program to create template in a wonderware system.
#First argument point to a mall how the template should be created, it can contains several templates.
#Mark the points that gonna be replaced with {0}, {1} and so on.
#Second argument point to the csv
#Rest of the arguments check with parmeter to replace {i} with.

import sys
import csv

srcFile = open(sys.argv[1], 'r')
keyFile = open(sys.argv[2], 'r')
output = open('output','w')

<<<<<<< HEAD
#var for dubblets
oldRow = []
first = True
=======
#Varibles for dublett
oldRow = []
oldTmp = []
first = True;
>>>>>>> checkforemptylines

template=srcFile.read()
keys = csv.reader(keyFile)
jump = False

for row in keys:        
    index = 3
    tmp = template
    result = []
    oldTmp = []
    while index < len(sys.argv):
        try:
            if (row[int(sys.argv[index])] == ""):
                jump = True
                break
            if (first == False):
                if (row[int(sys.argv[index])] == oldRow[index-2]):
                    jump = True
                    break
        except:
            jump = True
            break        
        result.append(row[int(sys.argv[index])])
<<<<<<< HEAD
        index = index +1
    if (oldRow!=result or first):
=======
        oldTmp.append(row[int(sys.argv[index])])
        index = index +1
        
        
>>>>>>> checkforemptylines
        if (jump == False):
            tmp = tmp.format(*result)
            print(tmp,file=output),
        else:
<<<<<<< HEAD
            print("Not a Value"),
    else:
        print("duplicate Row! Aborted row insert"),
    oldRow = result
    first = False
=======
            print("Inga giltiga värden"),
>>>>>>> checkforemptylines
    jump = False
    first = False
    oldRow = oldTmp
    
    
