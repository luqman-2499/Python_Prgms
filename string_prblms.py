# 1. Email Validation

# email = input("Enter your email: ") 
# if "@" in email and email.endswith(".com"): 
#     print("Valid Email") 
# else: 
#     print("Invalid Email")

###############################################

# 2. Count words in sentence

# sentence=input("enter a sentence: ")
# words=sentence.strip().split()
# print("total words:", len(words))

####################################################

# 3. String is palindrome or not

# text = input("Enter text to check for palindrome: ") 
# cleaned = text.replace(" ", "").lower() 
# if cleaned == cleaned[::-1]: 
#     print("Palindrome") 
# else: 
#     print("Not a palindrome")

######################################################

# 4. Fromat full name properly
 
# name = input("Enter your full name: ")
# formatted_name = name.strip().title() 
# print("Formatted Name:", formatted_name)

####################################################33

# 5. Password strength

# password = input("Enter your password: ") 
 
# if len(password) < 8: 
#     print("Weak Password: Too short") 
# elif password.isalpha() or password.isdigit(): 
#     print("Weak Password: Add numbers and letters") 
# else: 
#     print("Strong Password") 

#########################################################

# 6. Check string is titled or not

# text = input("Enter a title: ") 
# if text.istitle(): 
#     print("Properly titled") 
# else: 
#     print("Not titled correctly")

###################################################

# 7. Python program to Find Frequency of Each Character. 

# text = input("Enter a string: ") 
# text = text.replace(" ", "").lower() 
# char_freq = {} 
# for char in text: 
#     char_freq[char] = char_freq.get(char, 0) + 1 
# for char, freq in char_freq.items(): 
#     print(f"{char} : {freq}")

####################################################

# 8. phone = input("Enter phone number (10 digits): ") 
 
# if len(phone) == 10 and phone.isdigit(): 
#     masked = '*' * 6 + phone[-4:] 
#     print("Masked Phone:", masked) 
# else: 
#     print("Invalid phone number")

# ####################################################

# 9. Create username from full name

# full_name = input("Enter your full name: ") 
# username = ''.join(full_name.lower().split()) 
# print("Your username is:", username) 

#####################################################

# 10. Python program to Find and Replace Word in Sentence. 

# sentence = input("Enter a sentence: ") 
# old_word = input("Word to replace: ") 
# new_word = input("New word: ") 
 
# updated_sentence = sentence.replace(old_word, new_word) 
# print("Updated Sentence:", updated_sentence) 

#########################################################

# 11. Python program to Convert CSV Data to List. 

# data = input("Enter comma-separated values: ") 
# items = data.split(",") 
# print("List:", items) 

########################################################

# 12. Count No of Vowels in a word

# text = input("Enter a string: ").lower()

# vowels = "aeiou"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print("Total vowels:", count)

# ########################################################


