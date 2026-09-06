# ==============================
# PYTHON LIST OPERATIONS
# ==============================

# 1. Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)


# 2. Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# 3. Slicing: Exclude the last element char at index 4
print("Slice:", numbers[1:4])
print("First 3 elements:", numbers[:3])
print("Reverse:", numbers[::-1])


# 4. Changing an element
numbers[0] = 100
print("After changing element:", numbers)


# 5. Concatenation
list1 = [1, 2]
list2 = [3, 4]

print("Concatenation:", list1 + list2)


# 6. Repetition
print("Repetition:", list1 * 2)


# 7. Membership
print("Is 2 present:", 2 in list1)
print("Is 5 not present:", 5 not in list1)


# 8. Append: Adds one element at end 
numbers.append(60)
print("After append:", numbers)


# 9. Append a list:  whole new list iteself [70, 80] added in existing list
numbers.append([70, 80])
print("After append list:", numbers)


# 10. Extend: adds elements seperatly into existing list
numbers.extend([90, 100])
print("After extend:", numbers)


# 11. Insert: Insert elements at the index number specified 
numbers.insert(1, 15)
print("After insert:", numbers)


# 12. Count: How many times aappeared 
print("Count of 20:", numbers.count(20))


# 13. Index: Index position of 20 
print("Index of 20:", numbers.index(20))


# 14. Remove: removes by value
numbers.remove(20)
print("After remove:", numbers)


# 15. Pop: removes by index and returns in new string
removed = numbers.pop()
print("Removed element:", removed)
print("After pop:", numbers)


# 16. Reverse
numbers.reverse()
print("After reverse:", numbers)


# 17. Sort: sorts the list 
numbers.sort()
print("After sort:", numbers)


# 18. Sorted: sorts and returns a new sorted list
numbers2 = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers2)

print("Original list:", numbers2)
print("New sorted list:", sorted_numbers)


# 19. Built-in functions
print("Length:", len(numbers2))
print("Minimum:", min(numbers2))
print("Maximum:", max(numbers2))
print("Sum:", sum(numbers2))


# 20. Loop through list
print("List elements:")

for item in numbers2:
    print(item)


text = "Luqman"
# [Start : Stop : Step]
print(text[0:3])
print(text[:3])
print(text[2:])
print(text[:])
print(text[::-1])  # reverse start from last char "n"
print(text[::2])  # start from L leave 2 steps then print next char

# "Luq"
# "Luq"
# "qman"
# "Luqman"
# "namquL"
# "Lqa"