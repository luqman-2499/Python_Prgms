
# LOCAL FUNCTION 

# 1. Defining the function using "def" keyword with func name
def greet():
    print("Hello, welcome to the interview!")

# 2. Calling the function
greet()

##########################################################

# FUNCTION PARAMETERS AND ARGUMENTS

# 'a' and 'b' are PARAMETERS (placeholders to hold arg values)
def add_numbers(a, b):
    result = a + b
    print("The sum is:", result)


# 5 and 10 are ARGUMENTS (actual values passed to func def)
add_numbers(5, 10)


#########################################################


# FUNCTION WITH RETURN STMNT 

def add_numbers (a,b):
    sum = a + b
    return sum

result = add_numbers(2,2)
print("Sum is ",result)

###########################################################3

# PASSING SINGLE ARGUMENT TO FUNCTION
 
def add_numbers(a, b=5):  # b has a default value of 5
    return a + b

# Case 1: Passing both arguments (b gets overridden)
result1 = add_numbers(2, 10)
print(result1)  # Output: 12

# Case 2: Passing only one argument (b uses default value 5)
result2 = add_numbers(2)
print(result2)  # Output: 7 (2 + 5)

#############################################

# # PASSING ARGUMENT AS KEYWORD 


################################################

## GLOBAL FUNCTION

# x = 300

# def myfunction():
#   global x
#   x = 20
#   print(x)

# myfunction()

# print(x)

################################################

# x = 300

# def myfunction():
#   x = 200
#   print(x)

# myfunction()

# print(x)

####################################################


# Function to add two 1st name and last name

# def addname():
#     fname=input("Enter first name:")
#     lname=input("enter last name:")

#     sum=fname+" "+lname
#     print("the sum of",fname,"and",lname,"is:",sum)

# addname()

##################################################

# Add two names by passing arguments 

# def fullname(fname,lname):
#     fullname=fname+" "+lname
#     print(fullname)

# fname=input("enter first name:")
# lname=input("enter last name:")
# fullname(fname,lname)

###############################################

# display sum of numbers when num is passed as an argument

# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i
#     print(sum)

# num=int(input("Enter a number: "))
# sum(num)

###################################################


