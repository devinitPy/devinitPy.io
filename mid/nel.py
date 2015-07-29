#A file function that read a file
# marks=[]
file_name = "C:/Users/USER/devinitpy.github.io/mid/will.txt"

def open_file(name):
    file_name=open(name,"r")
    marks=file_name.readlines()
    print "from open file: "+str(marks)
    return marks

# open_file(file_name)


#grade for each mark in the list

def grade(marks_list):

    for mark in marks_list:
        print mark
        value = int(mark)

        if value> 80:
            grade = "A"
            print("grade for over 80: "+ grade)
        else:
            grade = "B"
            print("grade for btn 70 and 80: "+ grade)

marks_from_file=open_file(file_name)
grade(marks_from_file)



 #computes average of grades or marks
# def average(total,no)
#     y=total(t)/no
#     t=0
#     return t

#     # main function that puts all functions together
# def main():
#     data = open_file()
#     mark
#     mark=[]
#     marks=[]
#     names=[]
#     grade=[]

