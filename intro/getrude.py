def exam_scores():

    # Exam score and grades

    print("Welcome to the exam score  for your Maths,Science and English subjects ")

    print("enter your marks and view your scores")

    name=raw_input ('What is you name: ')

    maths_score=input ("Enter your Maths Marks" )
    science_score=input ("Enter your Science Marks")
    english_score= input (" Enter your English marks:")

    score=[english_score, maths_score, science_score]
    #to get total score
    #Create a variable that will store you total  score
    #initially total and average scores are 0
    total =0
    for x in score:
        if  x>= 95:
            grade="A"
        elif  x >= 75 and x < 95:
            grade="B"
        elif x >60 and x <75: #you had forgotten a colon here
            grade="C"
        elif x>45 and x<60: #you had forgotten a colon here
            grade="D"
        else:
            grade = "F"
        #compute new total score by adding current score to previous total score
        total=total + x
        print("you got grade {0} for score {1}".format(grade,x))
    print ("Total score is : {0}".format(total))
    #get average score

    return  total

#function to get average score
def averge_score(total_score,number_of_subjects):
    average= total_score/number_of_subjects
    print("Average score is : {0}".format(average))

#call our functions
exam_scores()
