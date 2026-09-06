
# # 1. Student Management System 


# # Dictionary structure: {Student Name: {Subject: Marks}}
# students = { 
#     "Anu": {"Math": 85, "Science": 90}, 
#     "Ravi": {"Math": 78, "Science": 88}, 
# } 
 
# def add_student(): 
#     name = input("Enter new student name: ").title() 
#     if name in students: 
#         print("Student already exists.") 
#         return 
#     students[name] = {} 
#     print(f"{name} added.") 
 
# def add_marks(): 
#     name = input("Enter student name: ").title() 
#     if name not in students: 
#         print("Student not found.") 
#         return 
#     subject = input("Enter subject: ").title() 
#     marks = int(input("Enter marks: ")) 
#     students[name][subject] = marks 
#     print(f"Marks added for {name} in {subject}.") 
 
# def view_marks(): 
#     name = input("Enter student name: ").title() 
#     if name not in students: 
#         print("Student not found.") 
#         return 
#     print(f"Marks for {name}:") 
#     for subject, mark in students[name].items(): 
#         print(f"  {subject}: {mark}") 
 
# def show_all(): 
#     for student, subjects in students.items(): 
#         print(f"\n{student}'s Marks:") 
#         for subject, marks in subjects.items(): 
#             print(f"  {subject}: {marks}") 
 
# def menu(): 
#     while True: 
#         print("\n----- Student Management -----") 
#         print("1. Add Student") 
#         print("2. Add Marks") 
#         print("3. View Student Marks") 
#         print("4. View All Students") 
#         print("5. Exit") 
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             add_student() 
#         elif choice == '2': 
#             add_marks() 
#         elif choice == '3': 
#             view_marks() 
#         elif choice == '4': 
#             show_all() 
#         elif choice == '5': 
#             print("Exiting program.") 
#             break 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu()


# #####################################################################


# # 2. Mini Shopping Cart System 


# Sample product list with prices 
products = { 
    "Laptop": 55000, 
    "Mobile": 20000, 
    "Headphones": 2000, 
    "Keyboard": 1500 
} 
 
# Shopping cart: {product_name: quantity} 
cart = {} 
 
def show_products(): 
    print("\nAvailable Products:") 
    for name, price in products.items(): 
        print(f"  {name}: ₹{price}") 
 
def add_to_cart(): 
    show_products() 
    item = input("Enter product name to add: ").title() 
    if item not in products: 
        print("Product not found.") 
        return 
    quantity = int(input("Enter quantity: ")) 
    if item in cart: 
        cart[item] += quantity 
    else: 
        cart[item] = quantity 
    print(f"{item} added to cart.") 
 
def view_cart(): 
    if not cart: 
        print("Cart is empty.") 
        return 
    print("\nYour Cart:") 
    total = 0 
    for item, qty in cart.items(): 
        price = products[item] 
        subtotal = price * qty 
        total += subtotal 
        print(f"  {item} x {qty} = ₹{subtotal}") 
    print(f"Total Amount: ₹{total}") 
 
def remove_from_cart(): 
    item = input("Enter product name to remove: ").title() 
    if item in cart: 
        del cart[item] 
        print(f"{item} removed from cart.") 
    else: 
        print("Item not in cart.") 
 
def menu(): 
    while True: 
        print("\n----- Shopping Cart -----") 
        print("1. Show Products") 
        print("2. Add to Cart") 
        print("3. View Cart") 
        print("4. Remove from Cart") 
        print("5. Checkout and Exit") 
        choice = input("Enter your choice: ") 
 
        if choice == '1': 
            show_products() 
        elif choice == '2': 
            add_to_cart() 
        elif choice == '3': 
            view_cart() 
        elif choice == '4': 
            remove_from_cart() 
        elif choice == '5': 
            print("Thank you for shopping!") 
            view_cart() 
            break 
        else: 
            print("Invalid choice. Try again.") 
 
menu()


#############################################################

# # 3. Library Book Management. 


# library = { 
#     "Python Basics": {"author": "John", "available": True}, 
#     "AI Fundamentals": {"author": "Ravi", "available": False} 
# } 
 
# def borrow_book(): 
#     name = input("Enter book name: ").title() 
#     if name in library and library[name]["available"]: 
#         library[name]["available"] = False 
#         print(f"You have borrowed '{name}'.") 
#     else: 
#         print("Book not available or not found.") 
 
# def return_book(): 
#     name = input("Enter book name to return: ").title() 
#     if name in library: 
#         library[name]["available"] = True 
#         print(f"'{name}' returned successfully.") 
#     else: 
#         print("Book not found in library.") 
 
# def display_books(): 
#     for title, details in library.items(): 
#         status = "Available" if details["available"] else "Issued" 
#         print(f"{title} by {details['author']} - {status}") 
 
# def menu(): 
#     while True: 
#         print("\n----- Library Sysytem -----") 
#         print("1. Borrow Book") 
#         print("2. Return Book") 
#         print("3. Display Books") 
         
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             borrow_book() 
#         elif choice == '2': 
#             return_book() 
#         elif choice == '3': 
#             display_books() 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu() 


###############################################################

# # 4. Employee Payroll System. 


# employees = { 
#     "E001": {"name": "Arun", "salary": 50000}, 
#     "E002": {"name": "Kavya", "salary": 60000} 
# } 
 
# def show_payslip(): 
#     eid = input("Enter employee ID: ").upper() 
#     if eid in employees: 
#         print(f"{employees[eid]['name']}'s Salary: ₹{employees[eid]['salary']}") 
#     else: 
#         print("Employee not found.") 
 
# def add_employee(): 
#     eid = input("Enter new employee ID: ").upper() 
#     name = input("Enter name: ").title() 
#     salary = int(input("Enter salary: ")) 
#     employees[eid] = {"name": name, "salary": salary} 
#     print("Employee added.") 
 
# def menu(): 
#     while True: 
#         print("\n----- Employee Payroll Syster -----") 
#         print("1. Show Payslip") 
#         print("2. Add Employee") 
         
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             show_payslip() 
#         elif choice == '2': 
#             add_employee() 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu()


###############################################################

# # 5. Online Quiz System. 


# quiz = { 
#     "What is the capital of India?": "Delhi", 
#     "Python is a ___ level language.": "High", 
#     "2 + 2 = ?": "4" 
# } 
 
# score = 0 
# for question, answer in quiz.items(): 
#     user_answer = input(question + " ").title() 
#     if user_answer == answer: 
#         score += 1 
 
# print(f"You scored {score}/{len(quiz)}")


################################################################

# # 6. Expense Tracker. 


# expenses = {} 
 
# def add_expense(): 
#     date = input("Enter date (dd-mm-yyyy): ") 
#     amount = float(input("Enter amount: ₹")) 
#     category = input("Enter category: ").title() 
#     expenses[date] = {"amount": amount, "category": category} 
#     print("Expense added.") 
 
# def view_expenses(): 
#     total = 0 
#     for date, data in expenses.items(): 
#         print(f"{date}: ₹{data['amount']} - {data['category']}") 
#         total += data['amount'] 
#     print(f"Total: ₹{total}") 
 
# def menu(): 
#     while True: 
#         print("\n----- Expenses Tracking -----") 
#         print("1. Add Expenses") 
#         print("2. View Expenses") 
     
         
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             add_expense() 
#         elif choice == '2': 
#             view_expenses() 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu()


#################################################################

# # 7. Movie Ticket Booking. 


# movies = { 
#     "Avengers": {"seats": 5}, 
#     "Batman": {"seats": 3} 
# } 
 
# def book_ticket(): 
#     movie = input("Enter movie name: ").title() 
#     if movie in movies and movies[movie]["seats"] > 0: 
#         movies[movie]["seats"] -= 1 
#         print(f"Ticket booked for {movie}!") 
#     else: 
#         print("No seats available or movie not found.") 
 
# def view_movies(): 
#     for movie, data in movies.items(): 
#         print(f"{movie} - Seats Left: {data['seats']}") 
 
# def menu(): 
#     while True: 
#         print("\n----- Movie Ticket Booking System -----") 
#         print("1. Book Ticket") 
#         print("2. View Movies") 
     
         
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             book_ticket() 
#         elif choice == '2': 
#             view_movies() 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu() 


#############################################################

# # 8. Railway Reservation System. 


# train = { 
#     "101": {"name": "Karnataka Express", "seats": 4}, 
#     "102": {"name": "Rajdhani Express", "seats": 2} 
# } 
 
# def reserve_ticket(): 
#     train_no = input("Enter train number: ") 
#     if train_no in train and train[train_no]["seats"] > 0: 
#         train[train_no]["seats"] -= 1 
#         print(f"Seat reserved in {train[train_no]['name']}") 
#     else: 
#         print("Train full or not found.") 
 
# def menu(): 
#     while True: 
#         print("\n----- Railway Reservation System -----") 
#         print("1. Book Ticket") 
         
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             reserve_ticket() 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu()

###############################################################

# # 9. Online Voting System. 


# candidates = { 
#     "Alice": 0, 
#     "Bob": 0, 
#     "Charlie": 0 
# } 
 
# def cast_vote(): 
#     vote = input("Vote for (Alice/Bob/Charlie): ").title() 
#     if vote in candidates: 
#         candidates[vote] += 1 
#         print("Vote cast successfully!") 
#     else: 
#         print("Invalid candidate.") 
 
# def show_results(): 
#     for name, count in candidates.items(): 
#         print(f"{name}: {count} votes") 
 
# def menu(): 
#     while True: 
#         print("\n----- Online Voting System -----") 
#         print("1. Cast Vote") 
#         print("2. Show Vote Result") 
     
         
#         choice = input("Enter your choice: ") 
 
#         if choice == '1': 
#             cast_vote() 
#         elif choice == '2': 
#             show_results() 
#         else: 
#             print("Invalid choice. Try again.") 
 
# menu() 

###########################################################

