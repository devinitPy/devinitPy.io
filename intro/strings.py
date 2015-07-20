'''
   Strings, lists manipulation
'''
# name = "allan"
# password="secret"
# print " your name is  {0}   password is {1} ".format(name,password)

# age = 12
# print "Are you %d of age? "%age
# print "user name is {0}and your password is {1} your age is {2}".format(name,password,age)
# print "Are you {0} of age? ".format(age)
# age_new = raw_input("users  age is: ")
# print(age_new)
# b = age_new+ 1
# print(b)

a = "university"
#print a.upper()
b="Lukwago Alex Betty"
identity= [a,b]
marks=[]

#length of a string
#open function
length=len(b)
print("length of b: {0}".format(length))
#method
c=b.split(" ")
print(c)

first_str= c[1]
print("split string {0}".format(first_str))
#chage case method
i = 0
for s in c:
    i=i+1
    upper=s.upper()
    print("Lower cased string: "+upper)
    print("upper cased string: {0}  {1} ".format(i,upper))
