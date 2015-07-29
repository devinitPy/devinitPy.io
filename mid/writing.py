print "Opening the file..."
filename="C:/Users/USER/devinitpy.github.io/mid/will.txt"
file = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")

print "And finally, we close it."
file.close()