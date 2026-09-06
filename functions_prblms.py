# def addnums(n1,n2):
#     sum=num1+num2
#     print("Sum of two numbers is: ",sum)

# num1=int(input("enter value of num1: "))
# num2=int(input("enter value of num2: "))
# addnums(num1,num2)

###########################################

# def evenodd(n):
#     if num%2==0:
#         print("EVEN")
#     else:
#         print("ODD")

# num=int(input("enter a number: "))
# evenodd(num)

###########################################

# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)

# num=int(input("Enter number: "))
# fact(num)

###########################################

# def max(a,b,c):
#     if a>b and a>c:
#         print("Max among three is A:",a)
#     elif b>c and b>a:
#         print("Max among three is B:",b)
#     else:
#         print("Max among three is C:",c)

# a=int(input("enter value of a: "))
# b=int(input("enter value of b: "))
# c=int(input("enter value of c: "))
# max(a,b,c)

##########################################

# def revstr(a):

#     reverse_string=""
#     for i in a:
#         reverse_string=i+reverse_string
#     print(reverse_string)

# a=input("Enter string: ")
# revstr(a)

############################################

# def count_vowels(string):
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     count=0
#     for i in string:
#         if i in vowels:
#             count+=1
#     print("string has ",count, "vowels")  
    

# string=input("enter string: ")
# count_vowels(string)

########################################################

# def farenhit(celcius):
#     farenhit= (celcius*9/5)+32
#     print("farenhit=", farenhit)

# celcius=int(input("Enter celcius: "))
# farenhit(celcius)

###############################################3

# def gcd(a,b):
#     while b:
#         a,b=b, a%b
#     return a

# num1=30
# num2=40
# print(gcd(num1,num2))

##############################################

# def longword(sentence):
#     words=sentence.split()
#     long= max(words, key=len)
#     print(long)

# sentence=input("enter a sentence: ")
# longword(sentence)

#################################################

# def is_anagram(str1,str2):
#     result=sorted(str1)==sorted(str2)
#     print (result)

# str1=input("enter string: ")
# str2=input("enter string2: ")
# is_anagram(str1,str2)

#################################################

# def second_largest(numbers):
#     unique_numbers=list(set(numbers))
#     unique_numbers.sort(reverse=True)
#     return unique_numbers[1] if len(unique_numbers)>1 else None

# print ("second largest", second_largest([10,20,30,40,80,90,40]))

#################################################################

