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

#A function that opens a file and returns data with in the file

file_location = "C:/Users/USER/devinitpy.github.io/week1/text.txt"
file_location1= "C:/Users/USER/devinitpy.github.io/week1/text2.txt"
file_location2 = "C:/Users/USER/devinitpy.github.io/week1/text3.txt"

files=[file_location,file_location1,file_location2]

def open_file(file_name):
    file=open(file_name,"r")
    data=file.readlines()
    return data

i =0
for i in range(0,3):
    current_file=files[i]
    d=open_file(current_file)
    i=i+1
    print(d)

# for item in data:
#     content =item.split(" ")
#     #print(content)
#     name=content[0]
#     marks=content[1]
#     print("name: "+name)
#     print("marks: "+marks)


# n =0
# for i in data:
#     n=n+1
#     list=i.split(" ")
#     if n == len(data) -1:
#         #we are on the last value
#         print("last for loop iteration")
#         #format it differently
#         print(list)
# file.close()
