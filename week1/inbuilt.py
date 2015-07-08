'''
    in built modules and freely available functions

'''
import math
import os,os.path

#string functions
name = "Lukwago"
#len function
print len(name)
#upper case
print name.capitalize()
if name.islower():
    print("string is lower case")
else:
    print("starts with upper case")
number = 12020.0990321
print math.floor(number)

for i in range (1, 8):
    print math.sqrt(i)

print os.getcwd()

print os.path.dirname("/week1/def.py")

file=open("C:/Users/USER/devinitpy.github.io/week1/oracle.txt","r")

data=file.readlines()

for i in data:
    print i
file.close()
