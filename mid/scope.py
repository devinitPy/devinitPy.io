'''
    A python program to illustrate variable scope
    variable in different scopes are different
    global variables can be read from local scope
    modifying globe scope from local scope

'''

#global variable
name = "Alex"

def nameFun():
    f_name = "allan"
    print("my name : "+f_name)
    print("global Name: "+name)

def newName():
    f_name = "lukwago"
    print("my name : "+name)

def modifyGlobal():
    global name
    #substring