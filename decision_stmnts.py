
## Find the greatest number among three using IF statements

a = int(input("Enter a= "))
b = int(input("Enter b= "))
c = int(input("Enter c= "))

if a > b and a > c:
    print("A is Greatest")  # A is greater than both B and C

elif b > a and b > c:
    print("B is Greatest")  # B is greater than both A and C

else:
    print("C is Greatest")  # C is greater than both A and B


# -----------------------------------------------------------


## Check voting eligibility using IF-ELSE statement

age = int(input("Enter your age: "))

if age >= 18:
    print("You are Eligible to Vote")  # Age is 18 or more, eligible
else:
    print("Not Eligible to Vote")  # Under 18, not eligible


# -----------------------------------------------------------


## Assign grade based on marks using ELIF ladder

marks = int(input("Enter Total Marks: "))

if marks > 85 and marks <= 100:
    print("Your Grade is A")  # Top grade
elif marks > 60 and marks <= 85:
    print("Your Grade is B")
elif marks > 40 and marks <= 60:
    print("Your Grade is C")
elif marks > 35 and marks <= 40:
    print("Your Grade is D")
else:
    print("Failed!!")  # Marks 35 or below means failed


# -----------------------------------------------------------


# # Nested IF statement to check driving eligibility

# # If first IF is true run next IF Stmnt else direct move to ELSE Stmnt 

age = int(input("Enter your age: "))

if age >= 18:
    # Eligible to drive if under 70
    if age >= 70:
        print("Can't Drive")  # Too old to drive
    else:
        print("You are Eligible")  # Between 18 and 69
else:
    print("You're Not Eligible")  # Under 18, not allowed


# -----------------------------------------------------------
