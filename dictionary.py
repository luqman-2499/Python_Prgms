# ==============================
# PYTHON DICTIONARY OPERATIONS
# ==============================

# 1. Creating Empty Dictionaries
# empty_dict1 = {}
# empty_dict2 = dict()

# print("Empty dictionaries:", empty_dict1, empty_dict2)


# 2. Creating a dictionary
students = {
    "Luqman": 85,
    "Ram": 41,
    "Riya": 95,
    "Ali": 57
}

print("Dictionary:", students)


# 3. Accessing value

print("Luqman's marks:", students["Luqman"]) # if the key doesn't exist can give Eror
print("Riya's marks:", students.get("Riya")) # .get() doesn't throw an error instead returns None


# 4. Adding a new element: One value at a time unlike update where multiple values can we added or updated
students["Mantesh"] = 73
print("After adding:", students)


# 5. Modifying an existing value
students["Ram"] = 88
print("After modifying:", students)


# 6. Membership
if "Luqman" in students:
    print("Luqman is present")

if "Khan" not in students:
    print("Khan not found")


# 7. Traversing keys
for key in students:
    print(key)


# 8. Traversing key and value: Items is used to print key and values
for key, value in students.items():
    print(key, ":", value)


# 9. Length
print("Length:", len(students))


# 10. Keys
print("Keys:", students.keys())


# 11. Values
print("Values:", students.values())


# 12. Items: .items() returns complete key value pairs
print("Items:", students.items())


# 13. Update: multiple balues add or update
students.update({"Zaid": 76})
print("After update:", students)


# 14. Delete using del
del students["Ali"]
print("After del:", students)


# 15. Pop: 
removed = students.pop("Ram")
print("Removed value:", removed)
print("After pop:", students)


# 16. Clear: empty whole string
students.clear()
print("After clear:", students)


# # MERGE 2 DICTIONARIES 

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {**d1, **d2}
print(merged)


####################################################################


# Create dictionary and perform operations 

# odd={1:'one',
#      3:'three',
#      5:'five',
#      7:'seven',
#      9:'nine'
#      }

# print(odd.keys())
# print(odd.values())
# print(odd.items())
# print(len(odd))
# print(7 in odd)
# print(2 in odd)
# print(odd.get(9))
# del odd[9]
# print(odd)

############################################################


# Enter names of employees and their salaries as input and store them in a dictionary

# num = int(input("Enter the number of employees whose data to be stored: ")) 
# count = 1 
# employee = dict() 
# while count <= num: 
#      name = input("Enter the name of the Employee: ") 
#      salary = int(input("Enter the salary: ")) 
#      employee[name] = salary 
#      count += 1 

# print("\n\nEMPLOYEE_NAME\tSALARY") 
# for k in employee: 
#      print(k,'\t\t',employee[k])


############################################################################

# prgm to count number of times a character has occured in string 

st = input("Enter a string: ") 
dictionary = {} 
for ch in st: 
     if ch in dictionary: 
          dictionary[ch] += 1
     else:
          dictionary[ch] = 1 
for key in dictionary: 
     print(key,':',dictionary[key])


######################################################################################



