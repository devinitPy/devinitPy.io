'''
Assement Test 1
    Each qn carries  10 marks, bonus qn carries 20 marks, Passmark is 50%
    Given a list containing dictionaries of students
    write  functions that interacts with the data as stated in the comments
'''

data = [{"name":"nelson","marks":70},
        {"name":"getrude","marks":85},
        {"name":"hana","marks":65},
        {"name":"emma","marks":55},
        {"name":"richard","marks":60},
        {"name":"sophie","marks": 90}]

#Qn1 . function that returns students average score
# dictionary_var = {"name":"nelson","marks":70}
# mark = dictionary_var.get("marks",0)
# mark = dictionary_var["marks"]
def student_scores(data_in):
    score_list = []
    for obj in data_in:
        mark = obj["marks"]
        score_list.append(mark)
    return score_list

scores = student_scores(data)
print (scores)

def summation(score_list):
    total = sum(score_list)
    average = total/len(score_list)
    print average

    

# Qn 2. function that returns a list of all the student names sorted in ascending order

#Qn3 . write a function that returns a students grade
#i.e grade = grading_function(data[0])

#Q4 write a function that adds to each student dictionary/object a grade attribute i.e data[0]={"name":"allan","marks": 70 , "grade": "B"}

#Bonus Question 5: sort the data list by student marks and return student with highest score
#hint https://wiki.python.org/moin/HowTo/Sorting
