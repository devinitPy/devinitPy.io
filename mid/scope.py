'''
    A python program to illustrate variable scope
    variable in different scopes are different
    global variables can be read from local scope
    modifying globe scope from local scope

'''

#global variable
name = "alex"



def nameFun():
    f_name = "allan"
    print("my name : "+f_name)
    print("global Name: "+name)
    return f_name;

def newName():
    f_name = nameFun();
    print("my name : "+f_name)
    print("global Name: "+name)

def modifyGlobal():
    last_name = "lukwago"
    full_name =last_name + " "+name
    #global name
    print(full_name)
   #n=last_name.capitalize()
    #print("in modify global: "+n)
    #substring

newName()
modifyGlobal()
nameFun()
