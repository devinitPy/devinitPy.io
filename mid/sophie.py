#this is a tuple why a tuple??

subjects=["Sociology", "Research", "Development"]


file_name = "C:/Users/USER/devinitpy.github.io/mid/will.txt"

def open_file(file_name):
    file=open(file_name, "r")
    data=file.readlines()
    print data
    return data

data=open_file(file_name)

for d in data:
    #Socioogy,B ,4 ,5
    item=d.split(",")
    first_item = item[0]
    print "first item is "+ first_item
    for sub in subjects:
        #print("subject in our subjects list: "+sub)
        if first_item== sub:
            print( "Subject: "+item[0])
            print( "grade: "+item[1])
            # print(d[0]+" score: "+d[2])




# list=["Sociology", "Research", "Development"]

# def computed_grade(Course_grade):
#     grade_value= None
#     grade_list=["F", "O", "D", "C", "B", "A"]
#     index=0
#     for g in grade_list:
#         index=index+1
#         if Course_grade == g:
#             grade_value=index
#         if grade_value== None:
#             print("wrong grade; Please re-enter your grade")
#             exam()
#         else:
#             print ("Your grade value is : "+str(grade_value))
#             return(grade_value)

# def determining_performance (grade):
#     if grade>=4:
#         print("good performance")
#     elif grade>=2 and grade <4:
#         print ("average score")
#     else:
#         print("poor performance")

# def exam():
#     #why are yoy doing this
#     raw_grade = list()
#     grade_value = computed_grade(raw_grade)
#     determining_performance(grade_value)

