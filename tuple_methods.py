# ==============================
# PYTHON TUPLE OPERATIONS
# ==============================

# 1. Creating a tuple
numbers = (2, 4, 6, 8, 10)

print("Tuple:", numbers)


# 2. Indexing
print("Element at index 3:", numbers[3])


# 3. Length
print("Length:", len(numbers))


# 4. Empty tuple
empty_tuple = tuple()
print("Empty tuple:", empty_tuple)


# 5. Creating tuple from string
vowels = tuple("aeiou")
print("Tuple from string:", vowels)


# 6. Creating tuple from list
list_data = [1, 2, 3, 4]
tuple_from_list = tuple(list_data)
print("Tuple from list:", tuple_from_list)


# 7. Creating tuple using range
range_tuple = tuple(range(5))
print("Tuple from range:", range_tuple)


# 8. Duplicates
values = (20, 30, 60, 10, 30, 10)

print("Count of 10:", values.count(10))


# 9. Index
print("Index of 10:", values.index(10))


# 10. Sorting a tuple
# sorted() returns a LIST
print("Sorted tuple:", sorted(values))


# 11. Tuple assignment
num1, num2 = (10, 20)

print("num1:", num1)
print("num2:", num2)


# 12. Assigning tuple values to variables
record = ("Luqman", "MCA", "2499")

name, course, roll_no = record

print("Name:", name)
print("Course:", course)
print("Roll No:", roll_no)


# 13. Swapping two numbers using tuple unpacking
num1 = 10
num2 = 20

print("Before swapping:", num1, num2)

num1, num2 = num2, num1

print("After swapping:", num1, num2)


# 14. Tuple slicing
data = (10, 20, 30, 40, 50)

print("Slice:", data[1:4])
print("Reverse:", data[::-1])


#########################################################


# PROGRAM TO SWAP 2 NBRS WITHOUT TEMP VARIABLE

# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))

# print("numbers before swapping: ")
# print (" first num:", num1)
# print("second num:", num2)
# (num1,num2)=(num2,num1)
# print("After swapping:", num1,num2)

############################################################

