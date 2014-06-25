Savior
======
Example:
myNamePattern
hello {0}

names.csv
 
New York,John

Paris, Smith
Stockhom, Johanna


python Savior --pattern myNamePattern --par 1 --output helloNames --file names.csv

=>

helloNames:

hello John
hello Smith
hello Johanna

This is very useful tool for creating instances from a template. 

