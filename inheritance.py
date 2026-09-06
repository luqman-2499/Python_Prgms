# Inheritance Example 

# class Animal: # Base Class
#     def speak(self):
#         print("Animal Speaking")
 
# class Dog(Animal): #Derived Class
#     def bark(self):
#         print("dog barking")
# d =Dog()
# d.bark()
# d.speak()



##########################################################



# MULTI LEVEL INHERITANCE

# class Animal:
#  def speak(self):
#     print("Animal Speaking")

# class Dog(Animal):
#   def bark(self):
#     print("dog barking....")

# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread...")

# d =DogChild()
# d.bark()
# d.speak()
# d.eat()


#######################################################


# MULTIPLE INHERITANCE

# class Calculation1:
#     def Summation(self,a,b):
#         return a+b;

# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b;

# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;
# d =Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))


##########################################################



# METHOD OVER RIDING

# class Animal:
#     def speak(self):
#         print("speaking")
 
# class Dog(Animal):
#     def speak(self):
#         print("Barking")

# d =Dog()
# d.speak()



#########################################################



#############   PROBLEMS  ########################

# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def show_info(self):
#         return f"Brand: {self.brand}, Speed: {self.speed} km/h"

# class Car(Vehicle):
#     def __init__(self, brand, speed, seats):
#         Vehicle.__init__(self, brand, speed)  # Calling parent constructor manually
#         self.seats = seats

#     def show_info(self):
#         return super().show_info() + f", Seats: {self.seats}"

# class Bike(Vehicle):
#     def __init__(self, brand, speed, type_of_bike):
#         Vehicle.__init__(self, brand, speed)
#         self.type_of_bike = type_of_bike

#     def show_info(self):
#         return super().show_info() + f", Type: {self.type_of_bike}"

# car = Car("Toyota", 180, 5)
# bike = Bike("Yamaha", 120, "Sport")

# print(car.show_info())  # Output: Brand: Toyota, Speed: 180 km/h, Seats: 5
# print(bike.show_info()) # Output: Brand: Yamaha, Speed: 120 km/h, Type: Sport



############################################################################



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def show_details(self):
#         return f"Product: {self.name}, Price: {self.price}"
    

# class Electronics(Product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty

#     def show_details(self):
#         return super().show_details() + f" Warranty: {self.warranty} years "


# class Grocery(Product):
#     def __init__(self, name, price, expiry_date):
#         super().__init__(name, price)
#         self.expiry_date = expiry_date

#     def show_details(self):
#         return super().show_details() + f" Expiry Date: {self.expiry_date} "

# laptop = Electronics("Laptop", 70000, 2)
# apple = Grocery("Apple", 200, "2025-06-15")

# print(laptop.show_details())
# print(apple.show_details())



###################################################################



# class LibraryItem:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def show_details(self):
#         return f"Title: {self.title}, Author: {self.author}"

# class Book(LibraryItem):
#     def __init__(self, title, author, pages):
#         super().__init__(title, author)
#         self.pages = pages

#     def show_details(self):
#         return super().show_details() + f", Pages: {self.pages}"

# class Magazine(LibraryItem):
#     def __init__(self, title, author, issue_number):
#         super().__init__(title, author)
#         self.issue_number = issue_number

#     def show_details(self):
#         return super().show_details() + f", Issue Number: {self.issue_number}"

# book = Book("Python Basics", "John Smith", 300)
# magazine = Magazine("Tech Monthly", "Jane Doe", 42)

# print(book.show_details())
# print(magazine.show_details())



###############################################################



# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def show_balance(self):
#         return f"{self.owner}'s balance: ${self.balance}"

# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def apply_interest(self):
#         self.balance += self.balance * self.interest_rate / 100

# account = SavingsAccount("Alice", 1000, 5)
# account.apply_interest()
# print(account.show_balance())  # Output: Alice's balance: $1050



#####################################################################3



# class Employee:
#     def __init__(self,name,salary):
#         self.name= name
#         self.salary= salary

#     def show_details(self):
#         return f"name: {self.name}, salary: {self.salary}"

# class Full_time_emp(Employee):
#     def __init__(self,name,salary,benefits):
#         super().__init__(name,salary)
#         self.benefits=benefits
    
#     def show_details(self):
#          return super().show_details() + f"benefits: {self.benefits}"
    

# fulltime= Full_time_emp("Luqman",50000,'Car')
# print(fulltime.show_details())



##################################################################3























