#Advanced Python

#Python Files

#open a file (in same directory)
f = open("message.txt")            #opens in read mode by default

#specify the mode in which we want to open the file
f = open("message.txt", "r")       #opens file in read mode
#f = open("message.txt", "w")       #opens file in write mode
#f = open("message.txt", "a")       #opens file in append mode


#read the contents of a file        #read() method
g = open("message.txt", "r")   #open the file

content = g.read()          #read all the content of the file
print(content)              #print the content

g.close()                   #close the file

#read a certain number of characters from the file
a = open("testfile.txt", "r")
contents = a.read(4)                #reads only first 4 characters of the file
print(contents)

#after reading upto 4th character, now start reading from next i.e. 5th character
remaining_contents = a.read(14)
print(remaining_contents)           #reads next 12 characters after 4th

#exception handling while working with files
# try..finally
try:
    a = open("testfile.txt", "r")

    contents = a.read(4)
    print(contents)

    remaining_contents = a.read(14)
    print(remaining_contents)
finally:
    a.close()

#using the 'with....open' syntax        #automatically closes the file without using 'finally' block
with open("testfile.txt", "r") as a:
    contents = a.read(4)
    print(contents)

    remaining_contents = a.read(14)
    print(remaining_contents)

#writing to files in python
#write to a file that doesn't exist (new file gets created)
with open("write.txt", "w") as b:
    b.write("Python is amazing\n")
    b.write("I love Python")                #new file 'write.txt' is created with the contents #Python is amazing
                                                                                               #I love Python

#if we open an existing file in write mode, the previous content of the file gets erased
c = open("write.txt", "r")
contents=c.read()
print(contents)                     #we can view the contents

d = open("write.txt", "w")          #contents are erased; can't be viewed

#append     #to add items to the end of the file without erasing its contents
print(content)      #message.txt file
with open("message.txt", "a") as app:
    app.write("\nI am learning Python.")
    app.write("\nThis is fun.")

#readlines() and writelines()
#readlines()
with open("message.txt","r") as test:       #open file in read mode
    lines = test.readlines()
    print(lines)                    #returns a list of the lines present in the file

#iterate through the list (to get each line, one by one)
for line in lines:
    print(line)

#writelines()
with open("names.txt", 'w') as name:
    text = ["My name is Mary.", "\nMy sister's name is June.", "\nWe live in a small village."]
    name.writelines(text)
    #new file names.txt gets created with the written content

    















