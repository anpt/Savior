#Copyright 2014 Anton Petersson

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#-------------------------------------------------------------------#

#Savior is a program to create template to a system.


import sys
import csv
import argparse

#Commandline funcionality
parser = argparse.ArgumentParser()
parser.add_argument("--pattern", help="File that contians the pattern for the template")
parser.add_argument("--file", help="csv file that contains data for insert in the pattern")
parser.add_argument("--par", type=int, nargs='+', help="list of parmater how to map pattern with the data in file, first column ")
parser.add_argument("--out", help="File to write the result to")
args = parser.parse_args();
#--------------------------#

srcFile = open(args.pattern, 'r')
keyFile = open(args.file, 'r')
output = open(args.out,'w')

#var for dubblets
oldRow = []
first = True


template=srcFile.read()
keys = csv.reader(keyFile)
jump = False

for row in keys:        
    index = 0
    tmp = template
    result = []
    oldTmp = []
    while index < len(args.par):
        try:
            if (row[int(args.par[index])] == ""):
                jump = True
                break
        except:
            jump = True
            break        
        result.append(row[int(args.par[index])])
        index = index +1
    if (oldRow!=result or first):        
        if (jump == False):
            tmp = tmp.format(*result)
            print(tmp,file=output),
        else:
            print("Not a Value"),
    else:
        print("duplicate Row! Aborted row insert. cont"),
    oldRow = result
    first = False
    jump = False
