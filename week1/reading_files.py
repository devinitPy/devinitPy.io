'''
    in built modules and freely available functions
'''
# import math
# import os,os.path

# #string functions
# name = "lukwago"
# #len function
# print len(name)
# #upper case
# print name.upper()
# if name.islower():
#     print("string is lower case")
# else:
#     print("starts with upper case")
# number = 12020.0990321
# print math.floor(number)

# for i in range (1, 8):
#     print math.sqrt(i)

#print os.getcwd()

#print os.path.dirname("/week1/def.py")

file=open("C:/Users/USER/devinitpy.github.io/week1/oracle.txt","r")

data=file.readlines()
#print(data)
n =0
for i in data:
    n=n+1
    list=i.split(" ")
    if n == len(data) -1:
        #we are on the last value
        print("last for loop iteration")
        #format it differently
        print(list)
file.close()
