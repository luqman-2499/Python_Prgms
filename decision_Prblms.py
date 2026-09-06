

## DECISION / CONDITIONAL STATEMENT PROBLEMS


# 1. Given Number Odd or Even

# num=int(input("Enter a Number: "))
# if num % 2 == 0:
#     print("Even Nummber")
# else:
#     print("Odd Number")


#############################################


# 2. Eligible to Vote

# age=int(input("Enter age: "))
# if age>=18:
#         print("Eligible to Vote")
# else:
#         print("Not Eligible to Vote")


##############################################


# 3. Divisible by 7 

# num=int(input("Enter a number: "))
# if num % 7 == 0:
#     print("Number is Divisbile by 7")
# else:
#     print("Number is Not Divisbile by 7")


##############################################


# 4. Print HELLO or BYE based on Multiple of 5

# num=int(input("Enter a Number: "))

# if num%5==0:  
#     print("Hello")
# else:
#     print("bye")


###############################################


# 5. Display Grade based on Percent

# percent=int(input("Enter Percentage: "))

# if percent>=80:
#     print("A+ Grade")

# elif percent<=80 and percent>=70:
#     print("A Grade")

# elif percent<=70 and percent>=60:
#     print("B Grade")

# elif percent<=60 and percent>=50:
#     print("C Grade")

# else:
#     print("FAILED!!")


###############################################


# 6. Calculate Body Mass Index

# height=float(input("Enter height in METER: "))
# weight=float(input("Enter Weight in KG: "))
# bmi=weight / (height * height)

# if bmi<=18.5:
#     print("UNDER WEIGHT")

# elif bmi>=18.5 and bmi<=25:
#     print("NORMAL WEIGHT")

# elif bmi>=25 and bmi<=30:
#     print("SLIGHTLY OVERWEIGHT")

# elif bmi>=30 and bmi<=35:
#     print ("OBESE")

# else:
#     print("Clinically OBESE")


############################################


# 7. Cost Price Of Bike Based on Road Tax

# price=int(input("Enter price of bike: "))

# if price>100000:
#     tax=price*15/100
#     print(tax)

# elif price>50000 and price<=100000:
#     tax=price*10/100
#     print(tax)

# elif price<=50000:
#     tax=price*5/100
#     print(tax)


#############################################


# 8.  A Year is LEAP or Not

# year=int(input("Enter a year: "))

# if year%4==0:
#     print("It is Leap Year")
# else:
#     print("Its not Leap Year")


##############################################


# 9. Accept a Number and display name of day 1 for sunday...

# num=int(input("Enter a number 1 to 7: "))

# if num==1:
#     print("Sunday")

# elif num==2:
#     print("Monday")

# elif num==3:
#     print("Tuesday")

# elif num==4:
#     print("Wednesday")


# elif num==5:
#     print("Thursday")


# elif num==6:
#     print("Friday")


# elif num==7:
#     print("Saturday")


############################################


#  11. Caluclate Electricty Bill

# units=int(input("Enter units:"))

# if units<=100:
#     print("No Charges")

# elif units>100 and units<=200:
#     price=(units-100)*5
#     print(price)

# elif units>200:
#     price=10*(units-200)
#     print(price)


#############################################


# 12. Display last digit of number

# num=int(input("Enter Number: "))
# num=num%10
# print('Num= ',+num)


#############################################


# 14. Accept City annd Display Monument

# city=input("Enter city: ")

# if city=="delhi":
#     print("Red Fort")

# elif city=="agra":
#     print("Taj Mahal")

# elif city=="jaipur":
#     print("Jai Mahal")


##############################################


# 16.Accept user attendance and display percent of attendance

# working=int(input("Enter no of working days: "))
# absent=int(input("Enter no of absent days: "))
# percent=(working-absent) / (working ) * 100
# print (percent)

# if percent>75:
#     print("Eligible for Exam ")

# else:
#     print("Not Eligible for Exam")


###############################################


# 17. Based on Salary and service print Bonus Amount

# salary=int(input("Enter salary: "))
# service=int(input("Enter years of service: "))

# if service>10:
#     bonus=salary*10/100
#     print(bonus)

# elif service>=6 and service<=10:
#     bonus=salary*8/100
#     print(bonus)

# elif service<6:
#     bonus=salary*5/100
#     print(bonus)


###############################################


# 18. Based on Marked price display net amount

# marked_price=int(input("enter marked price: "))

# if marked_price>10000:
#     discount=marked_price*20/100
#     print(discount)

# elif marked_price>7000 and marked_price<=10000:
#     discount=marked_price*15/100
#     print(discount)

# elif marked_price<=7000:
#     discount=marked_price*10/100
#     print(discount)


################################################


# 19. Based on sides Check which type of triangle 

# side_a=int(input("Enter side A: "))
# side_b=int(input("Enter side B: "))
# side_c=int(input("Enter side C: "))

# if side_a==side_b==side_c:
#     print("Equilateral Triangle")

# elif side_a!=side_b and side_b!=side_c and side_c!=side_a:
#     print("Scalene Triangle")

# elif side_a==side_b or side_b==side_c or side_c==side_a:
#     print("Isosceles Triangle")


#################################################


# 20. Using 2 inputs perform mathematical operators 

# num1=int(input("enter first number: "))
# num2=int(input("Enter second number: "))
# operator=input("enter operator: ")

# if operator=='+':
#     operator=num1+num2
#     print(operator)

# if operator=='-':
#     operator=num1-num2
#     print(operator)

# if operator=='*':
#     operator=num1*num2
#     print(operator)

# if operator=='/':
#     operator=num1/num2
#     print(operator)

# if operator=='%':
#     operator=num1%num2
#     print(operator)

# if operator=='//':
#     operator=num1//num2
#     print(operator)


############################################


# 21. Based on age and no of days display wages

# age=int(input("Enter your Age: "))
# gender=input("Enter your gender (M,F): ")
# days=int(input("Enter no fo days: "))

# if age>=18 and age<30 and gender=='m':
#     wage=days*700
#     print(wage)

# elif age>=18 and age<30 and gender=='f':
#     wage=days*750
#     print(wage)

# elif age>=30 and age<40 and gender=='m':
#     wage=days*800
#     print(wage)

# elif age>=30 and age<40 and gender=='f':
#     wage=days*850
#     print(wage)


###############################################


# 22. Accept number of days and Calculate Library  

# days=int(input("Enter no of Days: "))
# if days<=5:
#     charges=days*2
#     print(charges)

# elif days>5 and days<=10:
#     charges=days*3
#     print(charges)

# elif days>10 and days<=15:
#     charges=days*4
#     print(charges)

# elif days>15:
#     charges=days*5
#     print(charges)



##########################################


# 23. Accept km and calculate bill

# km=int(input("Enter kilometers: "))

# if km<=10:
#     bill=km*11
#     print(bill)

# elif km<=90:
#     bill=km*10
#     print(bill)

# if km>90:
#     bill=km*9
#     print(bill)


###############################################


#24. Accept marks and display stream alloted 

# eng=int(input("enter marks of english: "))
# maths=int(input("enter marks of maths: "))
# science=int(input("enter marks of science: "))
# social=int(input("enter marks of social: "))

# if eng>=80 and maths>=80 and science>=80 and social>=80:
#     print("Science Stream")

# elif eng>=80 and maths>=80 and science>=50 and social<=100:
#     print("Commerce Stream")

# elif eng>=80 and social>=80 and maths<=100 and science<=100:
#     print("Humanties Stream")



############################THE END################################

