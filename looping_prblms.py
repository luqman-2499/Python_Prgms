# 1. Print 1st 10 natural numbers FOR LOOP

# for i in range(1,11):
#     print(i)

##############################################

# 2. Print even numbers within given RANGE

# for num in range(12):
#     if num%2==0:
#         print(num)

################################################

# 3. Calculate sum of all num from 1 to given num

# i=int(input("Enter a number: "))

# sum=0

# for num in range(i+1):
#     sum+=num
# print(sum)
    
#################################################

#4. Multiplication

# num= int(input("Enter a number :"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

##########################################

# 5. Sum of all Odd Numbers

# num=int(input ("Enter number: "))
# sum=0
# for i in range(num):
#     if i % 2 ! = 0:
#         sum+=i
# print(sum)

###########################################

# 6. Display numbers from list using loop

# n=[10,20,30,40]
# for i in n:
#     print(i)

##############################################

# Count Total number of digits 

# num=100000
# num=str(num)
# count=0

# for i in num:
#     count+=1
# print(count)

##################################################

# Reverse Word 

# string=input("Enter string: ")
# reverse_string=""
# for i in string:
#     reverse_string=i+reverse_string
#     print(reverse_string)

# print("\n",reverse_string)


####################################################

# String Palindrome

# string="madam"
# reverse_string=""
# for i in string:
#     reverse_string=i+reverse_string
# if (string==reverse_string):
#     print("String", string,"is palindrome")
# else:
#     print("String", string,"is not palindrome")
 
#########################################################

# count number of even and odd numbers in series 

# list=[1,2,3,4,5,6,7,8,9,0]
# for i in list:
#     if i%2==0:
#         print(i," is even")
#     else:
#         print(i," is odd")

####################################################

# Display all numbers in range except prime numbers

# n=[2,4,7,9,10,14,17,20]
# for i in n:
#      if i%2==0:
#         print(i)

#####################################################

# Factorial of given number

# num=int(input("Enter number: "))
# fact=1

# for i in range(1,num+1):
#     fact=fact*i

# print(fact)

###################################################

# Fibonnaci series from o to 50

# num=4
# n1, n2 = 0, 1
# print("Fibonnaci series= ", n1, n2, end=" ")

# for i in range(2,num):
#     n3 = n1+n2 
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

################################################

#Print string and specify number of digits and letters in it

# string=input("enter string: ")
# digits=0
# letters=0

# for i in string:
#     if i.isdigit():
#         digits=digits+1

#     elif i.isalpha():
#         letters=letters+1

# print("the word", string,"has",letters, "letters and", digits,"digits")

###############################################################

# display number of days based on month 

# month=['may','april','feb']
# for i in month:
#     if i=="feb":
#         print("The month",i, "has 28 Days")
#     elif i in("april", "june", "september", "november"):
#         print("the month",i, "has 30 days")
#     elif i in ("january","march","may","july","august","october","december"):
#         print("The month", i,"has 31 days.")
#     else:
#         print("Invalid month")

###################################################################

# Print number pattern given by user

# num = int(input("Enter a number to generate its pattern = "))
# for i in range(1,num + 1):
#     for j in range(1,i + 1):
#         print("*", end = " ")
#     print()

####################################################################


        













































                                                                                                                                                                                                                              