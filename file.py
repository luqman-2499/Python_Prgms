
## Reading File 

# a= open("filesample.txt","r")
# if a:
#     print("file opened successfully")

################################################################


## Writing File (Removes all existing data and writes new content)

# file = open('filesample.txt','w')
# file.write("My name is Luqman Khan ")
 

######################################################################

## WITH statement ( No need to Close file if used with )

# with open("filesample.txt", "r") as file:
#     content = file.read()
#     print(content)

############################################################

## Writing into file and reading to print 

# with open("filesample.txt", "w") as file:
#     a=file.write("Hello, LUQMAN!\nWelcome to file handling in Python.")

# with open("filesample.txt", "r") as file:
#     content = file.read()
#     print(content)


#######################################################################


# fileptr = open("filesample.txt","r")
# # print(fileptr)
# #running a for loop
# for i in fileptr:
#     print(i) 

#####################################################

# file = open("filesample.txt","r")
# #stores all the data of the file into the variable content
# content = file.readline()
# #prints the content of the file
# print(content)
# #closes the opened file
# file.close()


##########################################################3


# a =["Hello\n", "python\n", "VictoryAcademy\n"]
# f1 = open('myfilesample.txt', 'w')
# f1.writelines(a)
# f1.close()
# f1 = open('filesample.txt', 'r')
# Lines = f1.read()
# count = 0
# for line in Lines:
#  count += 1
#  print("Line{}: {}".format(count, line.strip()))


#############################################################










