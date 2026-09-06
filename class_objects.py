
class Employee:

    # 2. __init__ is a method that runs automatically when we create an object of this class.
    # self refers to the current object and allows us to access/store the object's attributes and methods.

    def __init__(self, name, salary):
        self.name = name      # 3. Store name in the current object
        self.salary = salary  # 3. Store salary in the current object

    # 4. Method representing an action/behavior of the object
    def show(self):
        print(f'{self.name}: {self.salary}')  # 5. Print object's data


emp = Employee('Luqman', 5000)  # 1. Object is created; __init__ runs automatically
emp.show()                      # 4. Call the show() method


# # =============================
# # Program 1: Basic Person Class with Greet Method
# # =============================

class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def greet(self):
        print("Hello, my name is", self.name, "and my age is", self.age)

# Creating objects and calling greet method
p1 = Person("Mantesh", 27)
p1.greet()

p2 = Person("Lokesh", 28)
p2.greet()


# # =============================
# # Program 2: Class Variable Example
# # =============================

# class Person:
#     count = 0  # class variable to count number of objects

#     def __init__(self, name, age):
#         self.name = name  # instance variable
#         self.age = age
#         Person.count += 1  # increment class variable

# # Creating objects
# person1 = Person("Ayan", 25)
# person2 = Person("Bobby", 30)

# # Print total number of Person instances
# print(Person.count)


# # =============================
# # Program 3: Bank Account Class with Debit and Credit
# # =============================

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal  # store initial balance
#         self.account = acc  # store account number

#     def debit(self, amount):
#         self.balance -= amount  # subtract amount from balance
#         print("Debited amount is:", amount)
#         print("Total Balance is", self.getBalance())

#     def credit(self, amount):
#         self.balance += amount  # add amount to balance
#         print("Credited amount is:", amount)
#         print("Total Balance is", self.getBalance())

#     def getBalance(self):
#         print("Total Balance is", self.balance)
#         return self.balance

# # Create account and perform transactions
# acc1 = Account(23000, 1234567890)
# acc1.debit(5000)
# acc1.credit(1000)
# acc1.getBalance()


# # =============================
# # Program 4: Count Number of Students (Using Class Variable)
# # =============================

# class Student:
#     count = 0  # class variable

#     def __init__(self):
#         Student.count = Student.count + 1  # increment on each object creation

# # Create multiple student objects
# s1 = Student()
# s2 = Student()
# s3 = Student()

# # Display total count
# print("The number of students:", Student.count)


# # =============================
# # Program 5: Basic Class and Object with Method
# # =============================

# class Student:
#     def display(self):
#         print("this is student class")

# # Create object and call method
# s1 = Student()
# s1.display()


# # =============================
# # Program 6: Employee Class with Display Method
# # =============================

# class Employee:
#     def __init__(self, name, id, salary):
#         self.id = id  # instance variable
#         self.name = name
#         self.salary = salary

#     def display(self):
#         # f-string used to format output
#         print(f"id:{self.id}, name:{self.name}, salary:{self.salary}")

# # Create employee object
# e1 = Employee(101, 'John', 4000)
# e1.display()


# # =============================
# # Program 7: Simple Inventory System (Add, Update, Display)
# # =============================

# class Inventory:
#     def __init__(self):
#         self.items = {}  # initialize empty dictionary

#     def add_items(self, name, price, qty):
#         # Add item with name as key and price, qty as dictionary
#         self.items[name] = {"price": price, "qty": qty}

#     def dlt_items(self, name):
#         # Remove item if it exists
#         if name in self.items:
#             del self.items[name]

#     def update_items(self, name, price=None, qty=None):
#         # Update item details if it exists
#         if name in self.items:
#             if price:
#                 self.items[name]["price"] = price
#             if qty:
#                 self.items[name]["qty"] = qty

#     def display_inventory(self):
#         # Display all inventory items
#         for name, details in self.items.items():
#             print(f"{name}: {details}")

# # Create inventory and perform operations
# inventory = Inventory()
# inventory.add_items("laptop", 5000, 5)
# inventory.update_items("laptop", qty=4)
# inventory.display_inventory()


#####################################################################

