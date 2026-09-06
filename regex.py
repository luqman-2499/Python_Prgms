# Python has a built-in package called re, used to work wtih Regex.

# Import the re module:

##################################

# # MATCH => " Checks the string STARTS/BEGINS with pattern or not "

# import re

# Define a string and pattern to match 

# string = "Hello, world!"
# pattern = r"Hello"

# # Use re.match()
# match = re.match(pattern, string)

# # Check the result
# # Group returns only pattern if not used 
# # it will return regex object span length and pattern

# if match:
#     print("match found:", match)
#     print("Match found:", match.group())  
# else:
#     print("No match found")

##################################################################


# # SEARCH => 
# # " Searches in whole string and returns result wherever the pattern maybe present"

# import re

# # Define a pattern and string

# text = "my name is luqman and luqman is studying"
# pattern = r"luqman"

# # Use re.search()
# result = re.search(pattern, text)

# # Print result
# if result:
#     print("Match found:", result.group()) ## if exits multiple times returns only once 
# else:
#     print("No match found")

###########################################################################


# FINDALL => " Finds digits, all words and same word occured multiple times"
# Returns in form of list whether digit or words

# import re

# string = "my name is luqman and luqman is learning" # # case sensitive 
# pattern1 = r"luqman"  # # r => Ignore bakslashes treat as normal text only

# # FIND DIGITS (\d used for matching single digits) (\d+ used for matching searching multiple digits)

# digit= "There are 3 cats, 5 dogs, and 2 parrots."
# multi_digits= "There are 32 cats, 51 dogs, and 42 parrots."
# pattern2 = r"\d"
# pattern3=r"\d+"

# # \W+ FOR MULTIPLE WORDS

# text = "My name is Luqman."
# pattern4 = r"\w"
# pattern5=r"\w+"

# print("Matches found: ",re.findall(pattern1, string, re.IGNORECASE))
# print("digits found: ",re.findall(pattern2, digit))
# print("Multi_digits found: ",re.findall(pattern3, multi_digits))
# print("words found: ",re.findall(pattern4, text))
# print("words found: ",re.findall(pattern5, text))


# #  ADDITIONAL STMNTS 
# print("Number of times 'luqman' appears:", len(matches)) # COUNTS OCCURENCES 


########################################################################################


# # SPLIT =>"splits words with multiple seperators"

# import re

# text = "apple,banana;grape orange"
# sentence = "My-name,is.Luqman!"
# digit_split = "apple1banana2grape3"

# # Split on any comma, semicolon, or space and print 

# print(re.split(r"[;, ]", text))
# print(re.split(r"[-,.\s!]", sentence))
# print(re.split(r"\d",digit_split))

###################################################################################

# # SUBSTITUTE => "REPLACE ALL MATCHES OF PATTERN WITH NEW VALUES"

# import re

# digit = "My phone number is 994-539-1232"
# word = "luqman is learning!! and, luqman love's coding"

# # Replace all digits with # and replace words 

# print("Replace with # : ",re.sub(r"\d", "#", digit))
# print("Replace word: ",re.sub(r"luqman", "Usman", word))
# print("Replace punctuation: ",re.sub(r"[^\w\s]", "", word))

# # re.sub(r"[^\w\s]", "", => 
# # "any character that is NOT^ a letter, digit, underscore, or space" replace with ""


######################################################################################

# # FULLMATCH => it matches and checks whole string with pattern.
# # \w+ gives invalid if text contain symbol or spaces 

# import re

# text = "Luqman_123" # enter symbol or space to check No match 
# pattern = r"\w+"

# match = re.fullmatch(pattern, text)

# if match:
#     print("Full match found:", match.group())
# else:
#     print("No full match")

##################################################################################

# # VALID PIN CHECK 

# import re

# pin = "456789"
# pattern = r"\d{6}"  # Exactly 6 digits

# if re.fullmatch(pattern, pin):
#     print("Valid PIN")
# else:
#     print("Invalid PIN")

#############################################################################

# # re.finditer() returns an iterator of match objects.
# # Returns matched text &  start,end positions.

# import re

# text = "Luqman123 and Usman456 are learning Python789"
# pattern = r"\d+"

# matches = re.finditer(pattern, text)

# for match in matches:
#     print("Matched:", match.group())
#     print("Start:", match.start(), "End:", match.end())
#     print("------")

##############################################################################

# # ESCAPE => "searches and matches pattern that contain special symbols"

# import re

# text = "Today i spent $10.50 from my savings"
# pattern = re.escape("$10.50")  # treated as '\$10\.50'

# match = re.search(pattern, text)

# if match:
#     print("Found:", match.group())

###############################################################################

# # COMPILE => when u want to apply same pattern for multiple string texts 

# import re

# pattern = re.compile(r"\d")  # Compiled once 

# # # No need to create pattern for each text 

# text1 = "Cats: 3"
# text2 = "Dogs: 5"
# text3 = "Parrots: 2"

# print(pattern.findall(text1))
# print(pattern.findall(text2))
# print(pattern.findall(text3))

#################################################################################



# # PROGRAM : USER PROFILE ANALYZER


# import re

# # Compile all regex patterns
# digit_pattern = re.compile(r"\d")                    # At least 1 digit
# upper_pattern = re.compile(r"[A-Z]")                 # At least 1 uppercase
# lower_pattern = re.compile(r"[a-z]")                 # At least 1 lowercase
# symbol_pattern = re.compile(r"[^\w\s]")              # At least 1 special symbol
# length_pattern = re.compile(r".{8,}")                # At least 8 characters


# # Escape function demo - user entered special symbols
# user_input = "@admin*pass"
# escaped_input = re.escape(user_input)
# print(" Escaped user input (safe to search):", escaped_input)

# # Input password
# password = "Luqman@1232"


# # 1. Fullmatch - Check if password is exactly 8+ chars and valid
# if re.fullmatch(length_pattern, password):
#     print(" Password length is valid (8+ characters).")
# else:
#     print(" Password too short!")


# # 2. Search - check if password contains at least one uppercase
# if re.search(upper_pattern, password):
#     print(" Contains uppercase letter.")
# else:
#     print(" Missing uppercase letter.")



# # 2. Search - check if password contains at least one lowercase
# if re.search(lower_pattern, password):
#     print(" Contains lowercase letter.")
# else:
#     print(" Missing lowercase letter.")


# # 3. Match - check if password starts with a letter
# if re.match(r"[A-Za-z]", password):
#     print(" Starts with a letter.")
# else:
#     print(" Should start with a letter.")


# # 4. Findall - list all digits
# digits = re.findall(digit_pattern, password)
# print(" Digits found:", digits)


# # 5. Finditer - show symbols with positions
# print(" Special characters found:")
# for match in symbol_pattern.finditer(password):
#     print(f" Symbol: {match.group()} at position {match.start()}")


# # 6. Substitute - remove spaces if user adds by mistake
# cleaned_password = re.sub(r"\s+", "", password)
# print(" Cleaned password (no spaces):", cleaned_password)


# # 7. Split - simulate splitting password by any symbol
# split_result = re.split(r"[^\w]", password)
# print(" Split password parts:", split_result)


# # Final verdict
# if (
#     re.search(upper_pattern, password) and
#     re.search(lower_pattern, password) and
#     re.search(digit_pattern, password) and
#     re.search(symbol_pattern, password) and
#     re.fullmatch(length_pattern, password)
# ):
#     print("\n Strong Password!")
# else:
#     print("\n Weak Password. Improve your password security.")


####################################################################################################

