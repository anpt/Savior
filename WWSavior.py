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

#var for dubblets
oldRow = []
first = True

template=srcFile.read()
keys = csv.reader(keyFile)
jump = False

for row in keys:        
    index = 3
    tmp = template
    result = []
    
    while index < len(sys.argv):
        try:
            if (row[int(sys.argv[index])] == ""):
                jump = True
                break
        except:
            jump = True
            break        
        result.append(row[int(sys.argv[index])])
        index = index +1
    if (oldRow!=result or first):
        if (jump == False):
            tmp = tmp.format(*result)
            print(tmp,file=output),
        else:
            print("Not a Value"),
    else:
        print("duplicate Row! Aborted row insert"),
    oldRow = result
    first = False
    jump = False
    
    
