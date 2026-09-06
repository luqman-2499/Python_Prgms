
## READING OF FILE 

## If text file is saved in ur same python folder

# f = open("file_sample.txt")
# print(f.read())

############################################################

## WITH statement ( No need to Close file if used with )

# with open("file_sample.txt") as f:
#     content = f.read()
#     print(content)

############################################################


## Reads only specified characters of file from starting 

# with open("file_sample.txt") as f:
#     print(f.read(2))
###


## Reads only one line from the file 
## if u want to read two or more lines print f.readline multiple times  

# with open("file_sample.txt") as f:
#     print(f.readline())

###############################################################


## By looping through the lines of the file, 
## you can read the whole file, line by line:

# with open("file_sample.txt") as f:
#   for a in f:
#     print(a)

#############################################################


## APPEND OF FILE 'a' (adds new content from the end of cursor )

# with open("file_sample.txt", "a") as f:
#   f.write(" New content added with help of 'a' mode ")

# #open and read the file after the appending:
# with open("file_sample.txt") as f:
#   print(f.read())

###############################################################

## WRITING INTO FILE  'w' ( OVERWRITE INTO EXISTING FILE )
## whatever written in old file will be DELETED !!

# with open("file_sample.txt", "w") as f:
#   f.write("deletes old content and writes new one")

# #open and read the file after the overwriting:
# with open("file_sample.txt") as f:
#   print(f.read())

#################################################################


## CREATION OF FILE 'x'  ( if file exists errr occurs )

# f = open("newfile.txt", "x")

## DELETION OF FILE, we must use import os (if file not exists error msg ) 

# import os
# os.remove("text1.txt")

## To check file exists or not 

# import os
# if os.path.exists("text1.txt"):
#   os.remove("text1.txt")
# else:
#   print("The file does not exist")


###############################################################################

# file=open("text.txt","r+")
# a=file.read()
# print(a)
# file.write("abcd")
# print(a)
# file.close()

