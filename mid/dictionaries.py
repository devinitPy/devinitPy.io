
my_dictionary = { "name":"allan","school":"Makerere","physics":100,"biology":130}

#returns dictionry values
dictionary_values = my_dictionary.values()

my_school=my_dictionary["school"]
print my_school

value_list = []

for value in my_dictionary.values() :
      value_list.append(value)

 print value_list

 for key in my_dictionary.keys():
     print(key)

for item in my_dictionary.items():
    print(item)

 if "age" in my_dictionary:
    print my_dictionary["age"]

 #set age to zero if its not set
 my_age=my_dictionary.get("age", 0)
 my_height=my_dictionary.get("height", 1)

#adding new key value
 if "height" not in my_dictionary:
     my_dictionary["height"]=24
 print my_dictionary

#does same thing as get method but its faster
my_dictionary.setdefault("country","uganda")
print my_dictionary
