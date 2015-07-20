def exam_model():
    # introduction
    print("Welcome to the grade caluclator for you English, Science and Maths exams")
    print('type you scores in and find out your grades')
    name=raw_input ('What is you name: ')
    english_score= input ('What was your exam score for English:  ')
    maths_score=input ('What was your exam score for Maths:  ')
    Science_score=input ('What was your exam score for Science:  ')
    #its better to store your list of subjects in a variable
    score=[english_score, maths_score, Science_score]
    #you had forgotten to put a colons at the end of your for  and if loop statements
    total_score=0
    for i in score:
        if  i >= 90:
            grade="A"
        elif  i >= 80 and i < 90:
            grade="B"
        else:
            grade="C"
        total_score=total_score+ i
        #you can print your out put in all the various forms below
        print("you got grade {0} for score {1}".format(grade,i))
        #print("you got grade %s for score %d "%(grade,i))
        #print("you got grade: "+ grade+ " for score : "+str(i) )
#invoke or run our function
exam_model();
