
# ==============================
# PYTHON STRING METHODS
# ==============================

text = "   Luqman Khan Usman Hello Hello   "

# 1. Length
print("Length:", len(text))

# 2. Title: first letter of each word in uppercase
print("Title:", text.title())

# 3. Lowercase
print("Lower:", text.lower())

# 4. Uppercase
print("Upper:", text.upper())

# 5. Count:  No of Occurences, hello aappeared 2 times
print("Count of Hello:", text.count("Hello"))

# 6. Find
print("Find Hello:", text.find("Hello"))
print("Find Python:", text.find("Python"))  # -1 if not found

# 7. Index: returns index number if not found returns -1 and ValueError
print("Index of Hello:", text.index("Hello"))


# 8. Startswith: Returns boolean value checks starts with cahr
print("Starts with letter A:", text.startswith("A"))

# 9. Endswith: checks ends with which char
print("Ends with letter X:", text.endswith("X"))

# 10. isalnum():  checks string is in number + char or not
word = "Luqman123"
print("Is alphanumeric:", word.isalnum())

# 11. isalpha(): checks string is in only alpha no numbers 
name = "Luqman"
print("Is alphabetic:", name.isalpha())

# 12. isdigit()
number = "12345"
print("Is digit:", number.isdigit())

# 13. islower()
print("Is lowercase:", name.islower())

# 14. isupper()
print("Is uppercase:", name.isupper())

# 15. Replace
print("Replace:", text.replace("Hello", "Hi"))

# 16. Strip: removes spaces and returns in new string
clean_text = text.strip()
print("Strip:", clean_text)

# 17. Split: splites string into list of aarray
words = clean_text.split()
print("Split:", words)

# 18. Join: combine with given chars
print("Join:", "-".join(words))