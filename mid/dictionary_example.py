'''
iterate through the list
print each object/dictionary entry

'''
import math,functools
import os
import json


mylist= [{"name":"allan","maths":20,"class":"S2"},{"name":"alex","maths":89,"class":"s3"},
{"name":"alex","maths":89,"class":"s3"}]

# my_dictionary={"math":[45,50,60],"students":["alex","allan","betty"]}

student_1 =mylist[0]
student_2 = mylist[1]

total = student_1["maths"] + student_2["maths"]

my_total = 0

for student in mylist:
    mark = student["maths"]
    my_total=my_total + mark


math.sqrt(my_total)