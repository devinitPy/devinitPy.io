def sum():
    print "sum function with no arguments"
    a=2
    b=3
    c= a+b
    print "sum is {0}".format(c)
sum()

def summation(a,b):
    print "sum function with arguments"
    c=a+b
    print "sum is {0}".format(c)
summation(5,6)

def sumReturn(a,b):
    print "sum function with arguments"
    c=a+b
    return c
d=sumReturn(2,3)
print "d is assigned return value of summation funtion,  d is %d"%d
#global variables
name = "allan"

def nameFun():
    print("global name is : "+name)
    n= "alex"
    print("local name is : "+ n)