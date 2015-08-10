'''
    script that reads students marks from a file
    computes their grades and gets total and average score
    remove the pass key word after writing your code for each function
'''
#"Welcome to the exam score  for your Maths,Science and English subjects"
# open file function that opens files

# name =input('what is your name'):
# def name ()
# print ('hello'+ name)

print("Welcome to the exam score  for your Economics,Financial Mg't and Auditing ")

print("enter your marks for each of the course units and we will grade you accordingly")

lines=[]
gra=[]

file_name = "C:/Users/USER/devinitpy.github.io/mid/getrude.txt"

def open_file (file_name):
    file=open(file_name, "r")
    lines=file.readlines()
    return lines
    #returns marks list

  # computes grade  for each mark in the list
def grade(marks):
    gra=[]
    for j in marks:
        value = int(j)
        if value>= 95:
            grade="A"
        elif  value >= 75 and value< 95:
            grade="B"
        elif value >60 and value <75:
            grade="C"
        elif value>45 and value<60:
            grade="D"
        else:
            grade = "F"
        gra.append(grade)
        #gra=gra+[grade]
    return gra
    # returns list of computed grade

def main():
    data=[]
    subject=[]
    mar=[]
    g=[]
    data = open_file(file_name)
    for y in data:
        x = y.split(" ")
        subject=subject+[x[0]]
        mar=mar+[x[1]]

    print subject
    print mar

    g=grade(mar)
    print g

    # grade_list =computeGrade(data)
    # total_grades = total(grade_list)
    # number_of_subjects =len(grade_list)
    # average_grades = average(total_grades,number_items)
main()