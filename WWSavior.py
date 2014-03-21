import sys
import csv

srcFile = open(sys.argv[1], 'r')
keyFile = open(sys.argv[2], 'r')
output = open('output','w')

template=srcFile.read()
keys = csv.reader(keyFile)


for row in keys:        
    index = 3
    tmp = template
    result = []
    while index < len(sys.argv):
        result.append(row[int(sys.argv[index])]) 
        index = index +1
    
    tmp = tmp.format(*result)
    print(tmp,file=output),

