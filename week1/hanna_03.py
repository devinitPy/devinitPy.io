
name=raw_input("what is your name? ")
english_mark=input("what is your english mark? ")
maths_mark=input("what is your maths mark? ")
science_mark=input("what is your science mark? ")

all_marks=[english_mark, maths_mark, science_mark]

for x in all_marks:
    if x>=80:
        score=5
    elif 60>= x <=79:
        score=4
    else:
        score=3


print("your total score for english is: %s") % {english_mark}

# combined_grade=grade+grade+grade
# average_score=(score+score+score)/3
# total_score=score+score+score

# print("combined grade is %s")%combined_grade
# print("average score is %d")%average_score
# print("total score is %d")%total_score