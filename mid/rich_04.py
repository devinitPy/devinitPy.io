
file_location="C:/python_tutorials/exam_scores3.txt"

def open_file(file):
    file=open(file_location, "r")
    data=file.readlines()
    return data


def list_sort (list):

    #what is i?? i is undefined
    names = []
    #we normally return at the end of a function
    for d in list:
        names=[i.split(' ,', 1)[0] for i in d]

    # names=[i.split(',', 1)[0] for i in names]
    # scores=[i.split(' ,', 3)[0] for i in d]
    # scores=[i.split(',', 3)[0] for i in names]
    # keith_data = newlist[0:1]
    # sophie_data = newlist[1:2]
    # nelson_data = newlist[2:3]
    # keith_scores = keith_data[0:2]
    # print scores
    # print names
    # print newlist
    print keith_scores

data=open_file(file_location)
list_sort(data)

# def isNumber(s):
#     try:
#         int(s)
#         return True
#     except:
#         return False

# splitstr = [substr.strip().split(' ') for substr in newlist.split(',')]
# for pair in splitstr:
#     if len(pair)>1:
#         if isNumber(pair[1]):
#             number = int(pair[1])
#         else:
#             number = "Is not a number"
#     else:
#         number = "There is no number"
#     print(pair[0],number)

# newlist()