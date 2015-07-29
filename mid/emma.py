#importing all data files I will use for this programme.
file_location="C:/Users/USER/devinitpy.github.io/mid//keith_scores.txt"
file_location1="C:/Users/USER/devinitpy.github.io/mid/sophie.txt"
file_location2="C:/Users/USER/devinitpy.github.io/mid/will.txt"


#separating the student marks
keith_scores=file_location
Sophie_scores=file_location1
richard_scores=file_location2


files=[keith_scores,Sophie_scores,richard_scores]
#list that will contain each students data
data = []
#opening the files
def open_file(files):
    file=open(files, "r")
    data=file.readlines()
    print (data)
    return data

i=0
for i in range (0,3):
    current_file=files[i]
    i=i+1
    d=open_file(current_file)
    #add the returned data to the data list
    data.append(d);

print ("Keiths data "+ str(data[0]))
print ("sophies data "+ str(data[1]))
print ("richards data "+ str(data[2]))
