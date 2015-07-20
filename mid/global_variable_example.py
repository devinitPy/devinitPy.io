
#A Function that gets the course data and returns the course raw grade
#if this function is called a second time because the user inputed a wrong grade value
#it skips asking for the users name and course unit
#this is because the counter variable which we use to track how many times the
#course data function is being called will no longer be Zero
counter  = 0

def course_data():
    # the word global infront of counter tells python we are refering to the counter
    # variable defined outside this function
    # we shall study more about global variables when we study about function scopes
    globxal counter
    if counter == 0:
        #ask for user name course etc if counter is 0
        name=raw_input("Name: ")
        course=raw_input("Course: ")
        course_unit=raw_input("course_unit1: ")
        counter=counter+1
    else:
        print("You already gave us your details Just get us Your grade: ")
    grade=raw_input("Course Grade: ")
    return grade

#function that gets the computed grade (logic)
def computed_grade(user_grade):
    # definining grade value variable as an intially empty variable
    grade_value = None
     #The index of the element corresponds to its value
    grade_list = ["A","B","C","D","E"]
    index = 0
    for g in grade_list:
        index=index+1
        if user_grade == g :
            grade_value = index
    # user entered invalid grade that we dont have in our list
    if grade_value == None:
        print("entered wrong grade, Please re-enter your grades one more Time: ")
        exam()
    else:
          print ("Your grade value is : "+str(grade_value))
          return grade_value

def determining_performance(grade):
    if grade >= 4:
        print("good performance")
    elif  grade >=2 and grade < 4:
        print("average score")
    else:
        print("poor performance")

#putting all our function in one function so that we make only one function call to run our progra
def exam():
    raw_grade = course_data()
    grade_value=computed_grade(raw_grade)
    determining_performance(grade_value)
#run our program
exam()