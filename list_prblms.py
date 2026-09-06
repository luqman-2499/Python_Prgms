
# 1. Student Result Processing System 
# Use Case: Calculate average marks, assign grades, and display the top performer.


# students = [ 
#     ['John', [88, 76, 92]], 
#     ['Alice', [85, 90, 80]], 
#     ['Bob', [70, 60, 75]] 
# ] 
 
# def calculate_grade(avg): 
#     if avg >= 85: 
#         return 'A' 
#     elif avg >= 70: 
#         return 'B' 
#     else: 
#         return 'C' 
 
# topper = None 
# highest_avg = 0 
 
# for student in students: 
#     name, marks = student 
#     avg = sum(marks) / len(marks) 
#     grade = calculate_grade(avg) 
#     print(f"{name} - Average: {avg:.2f}, Grade: {grade}") 
     
#     if avg > highest_avg: 
#         highest_avg = avg 
#         topper = name 
 
# print(f"\nTopper: {topper} with average {highest_avg:.2f}")


################################################################

# 2. Grocery Store Inventory Tracker 
# Use Case: Add, remove, search, and sort grocery items with prices.

# inventory = [ 
#     ['Apples', 50], 
#     ['Bananas', 20], 
#     ['Milk', 30], 
#     ['Bread', 25] 
# ] 
 
# # Add new item 
# inventory.append(['Eggs', 40]) 
# print("after adding new item: ", inventory)
 
# # Remove item 
# inventory = [item for item in inventory if item[0] != 'Bananas'] 
# print("after removing banana: ", inventory)

# ANOTHER WAY 
# new_inventory = []
# for item in inventory:
#     if item[0] != 'Bananas':
#         new_inventory.append(item)
# inventory = new_inventory

 
# Search item 
# item_to_find = 'Milk' 
# found = next((item for item in inventory if item[0] == item_to_find), None) 
# if found: 
#     print(f"{item_to_find} found: Price = ₹{found[1]}") 
# else: 
#     print(f"{item_to_find} not found.") 
 
# Sort by price 
# inventory.sort(key=lambda x: x[1]) 
 
# print("\nSorted Inventory by Price:") 
# for item in inventory: 
#     print(f"{item[0]} - ₹{item[1]}")


##############################################################

# 3. Movie Ticket Booking System 
# Use Case: Keep track of available seats and booked seats. 

# total_seats = list(range(1, 11))  # Seats 1 to 10 
# booked_seats = [] 
 
# # Book seat 
# def book_seat(seat_no): 
#     if seat_no in total_seats and seat_no not in booked_seats: 
#         booked_seats.append(seat_no) 
#         total_seats.remove(seat_no) 
#         print(f"Seat {seat_no} booked successfully.") 
#     else: 
#         print(f"Seat {seat_no} is not available.") 
 
# # Booking examples 
# book_seat(3) 
# book_seat(5) 
# book_seat(3)  # Already booked 
 
# print("\nAvailable seats:", total_seats) 
# print("Booked seats:", booked_seats) 


###########################################################

# 4. Hotel Room Booking System 
# Use Case: Track booked and available rooms (1–10), and prevent double booking. 

# all_rooms = list(range(1, 11)) 
# booked_rooms = [] 
 
# def book_room(room_no): 
#     if room_no in all_rooms and room_no not in booked_rooms: 
#         booked_rooms.append(room_no)
#         all_rooms.remove(room_no) 
#         print(f"Room {room_no} booked successfully.") 
#     else: 
#         print(f"Room {room_no} is already booked or invalid.") 
 
# book_room(3) 
# book_room(5) 
# book_room(3)  # Try booking again 
 
# print("Booked Rooms:", booked_rooms) 
# print("Available Rooms:", all_rooms)


#####################################################################

# 5. Bus Seat Reservation System 
# Use Case: Show available seats, reserve a seat, and prevent duplicate bookings.

# seats = ['A1', 'A2', 'A3', 'B1', 'B2'] 
# reserved = [] 
 
# def reserve(seat): 
#     if seat in seats and seat not in reserved: 
#         reserved.append(seat) 
#         # seats.remove(seat) #if u want to print seats and reserved without creating show_seats() function
#         print(f"Seat {seat} reserved.") 
#     else: 
#         print(f"Seat {seat} is already reserved or does not exist.") 
 
# def show_seats(): 
#     print("Available:", [s for s in seats if s not in reserved]) 
#     print("Reserved:", reserved) 
 
# reserve('A1') 
# reserve('B2') 
# reserve('A1')  # Already reserved 
# show_seats()
# # #if u want to print without using show_seats() function
# print(seats)
# print(reserved)
################################################################

# 6. Attendance Tracker for a Week 
# Use Case: Track daily presence and calculate weekly attendance percentage.


# students = ['Amit', 'Sara', 'Rohan'] 
# attendance = { 
#     'Amit': [1, 1, 1, 0, 1], 
#     'Sara': [1, 0, 1, 1, 1], 
#     'Rohan': [0, 1, 1, 0, 0] 
# } 
 
# for name in students: 
#     Total_days_present= sum(attendance[name]) 
#     percentage = (Total_days_present / 5) * 100 
#     print(f"{name} - Present: {Total_days_present}/5 days, Attendance: {percentage:.0f}%")


#####################################################################

# 7. Library Book Management System 
# Use Case: Add new books, search books by title, and remove a book when issued.

 
# def add_book(title): 
#     if title not in library: 
#         library.append(title) 
#         print(f"'{title}' added to library.") 
#     else: 
#         print(f"'{title}' is already in the library.") 
 
# def issue_book(title): 
#     if title in library: 
#         library.remove(title) 
#         print(f"'{title}' issued.") 
#     else: 
#         print(f"'{title}' is not available.") 
 
# def search_book(title): 
#     return title in library 
 
# # Usage
# library = ['The Alchemist', 'Rich Dad Poor Dad', '1984', 'Clean Code']  
# add_book('Atomic Habits') 
# issue_book('1984') 
# print("Searching for 'Clean Code':", search_book('Clean Code')) 
# print("Available Books:", library) 


#################################################################

# 8. Employee Management System 
# Use Case: Store employees with their departments and find employees by department.


# employees = [ 
#     ['Amit', 'HR'], 
#     ['Sara', 'IT'], 
#     ['John', 'Finance'], 
#     ['Meena', 'IT'] 
# ] 
 
# def get_by_department(dept): 
#     return [emp[0] for emp in employees if emp[1] == dept] 
 
# print("Employees in IT:", get_by_department('IT'))

##############################################################

# 9. Restaurant Order System 
# Use Case: Accept customer orders, cancel an order, and show the final bill.


# menu = { 
#     'Burger': 100, 
#     'Pizza': 250, 
#     'Fries': 70 
# } 
# orders = [] 
 
# def place_order(item): 
#     if item in menu: 
#         orders.append(item) 
#         print(f"{item} ordered.") 
#     else: 
#         print(f"{item} is not on the menu.") 
 
# def cancel_order(item): 
#     if item in orders: 
#         orders.remove(item) 
#         print(f"{item} canceled.") 
#     else: 
#         print(f"{item} was not in the order.") 
 
# def show_bill(): 
#     total = sum(menu[item] for item in orders) 
#     print("Final Order:", orders) 
#     print("Total Bill: ₹", total) 
 
# # Example usage 
# place_order('Pizza') 
# place_order('Fries') 
# cancel_order('Burger') 
# place_order('Burger') 
# show_bill()

############################################################

# 10. Online Poll System 
# Use Case: Users vote for an option, and the system shows the result with counts.

# options = ['Python', 'Java', 'C++'] 
# votes = [0, 0, 0] 
 
# def vote(option): 
#     if option in options: 
#         index = options.index(option) 
#         votes[index] += 1 
#     else: 
#         print("Invalid option") 
 
# vote('Python') 
# vote('Python') 
# vote('Java') 
# vote('C++') 
# vote('Python') 
 
# # Results 
# for i in range(len(options)): 
#     print(f"{options[i]}: {votes[i]} votes")

#############################################################

# 11. Online Course Enrollment System 
# Use Case: Track course registrations, avoid duplicate enrollments, 
# and count course-wise enrollments.

# courses = { 
#     'Python': [], 
#     'Java': [], 
#     'Web Dev': [] 
# } 
 
# # Enroll students 
# enrollments = [ 
#     ('Alice', 'Python'), 
#     ('Bob', 'Java'), 
#     ('Alice', 'Web Dev'), 
#     ('Bob', 'Python'), 
#     ('Alice', 'Python')  # Duplicate 
# ] 
 
# for name, course in enrollments: 
#     if name not in courses[course]: 
#         courses[course].append(name) 
 
# # Display enrollments 
# for course, students in courses.items(): 
#     print(f"{course}: {len(students)} students -> {students}")


#############################################################

# 12. Sales Performance Tracker
 

# employees = [ 
#     ["Alice", [1000, 1200, 900]], 
#     ["Bob", [800, 950, 1050]], 
#     ["Charlie", [1100, 1150, 950]], 
# ] 
 
## Total sales for each employee
 
# for emp in employees: 
#     total = sum(emp[1]) 
#     print(f"{emp[0]} - Total Sales: ₹{total}") 
 
## Highest single-day sale
## max(sale, emp[0]) --> [(1000, 'Alice'), (1200, 'Alice'), (900, 'Alice'), ..., (950, 'Charlie')]

# high_sale = max([(sale, emp[0]) for emp in employees for sale in emp[1]]) 
# print(f"Highest Single Day Sale: ₹{high_sale[0]} by {high_sale[1]}")

# highest_sale=0
# emp_name=''
# for emp in employees:
#     for sale in emp[1]:
#         if sale>highest_sale:
#             highest_sale= sale
#             emp_name=emp[0]
         
 
# # Best performing employee 
# # X is each individual element ("alice", [100,200]) in employees 
# # the function loops each list and performs sum for each

# best = max(employees, key=lambda x: sum(x[1]))
## max returns a list of max among all the list eg: max= [charlie, [100,200,300]] 
# print(f"Top employeee: {best[0]} with ₹{sum(best[1])}")


############################################################

# 13. COVID Vaccination Slot Tracker. 

# centers = [ 
#     ["Center A", [10, 0, 5]], 
#     ["Center B", [2, 1, 0]], 
#     ["Center C", [8, 5, 6]], 
# ] 
 
# # Total slots per center 
# for center in centers: 
#     print(f"{center[0]} - Total Slots: {sum(center[1])}") 
    
# # Center with max slots 
# max_center = max(centers, key=lambda x: sum(x[1])) 
# print(f"Most Available Center: {max_center[0]} with total slots = {sum(max_center[1])}") 
 
# # Day-wise availability 
# days = ["Day 1", "Day 2", "Day 3"] 
# # for i in range(3): 
# #     print(f"\n{days[i]} Slot Availability:") 
# #     for center in centers: 
# #         print(f"{center[0]}: {center[1][i]}")

# for i in days:
#     print(i, 'Slot Availability:')
#     for center in centers:
#         print(f" {center[0]}: {sum(center[1])}")


############################################################

# 14.  Online Order Delivery Tracker. 


# orders = [ 
#     [1001, "Ravi", ["Shoes", "Socks"], False], 
#     [1002, "Neha", ["Laptop"], True], 
#     [1003, "Ravi", ["T-shirt", "Cap", "Watch"], False], 
# ] 
 
# def undelivered_orders(): 
#     return [o for o in orders if o[3]==False] # can also write as if not o[3]
 
# def items_by_customer(name): 
#     count = 0 
#     for o in orders: 
#         if o[1].lower() == name.lower(): 
#             count += len(o[2]) 
#     return count 
 
# def mark_delivered(order_id): 
#     for o in orders: 
#         if o[0] == order_id: 
#             o[3] = True 
#             return f"Order {order_id} marked as delivered" 
#     return "Order ID not found" 
 
# print("Pending Orders:", undelivered_orders()) 
# print("Total Items Ordered by Ravi:", items_by_customer("Ravi")) 
# print(mark_delivered(1003))


#############################################################

# 15.Employee Attendance Management System. 

# employees = [ 
#     ["E101", "Alice", ["P", "A", "P", "P", "A"]], 
#     ["E102", "Bob", ["P", "P", "P", "P", "P"]], 
#     ["E103", "Charlie", ["A", "A", "P", "P", "P"]], 
# ] 
 
# def attendance_percentage(attendance): 
#     total_days = len(attendance) 
#     present_days = attendance.count("P") 
#     return (present_days / total_days) * 100 
 
# for emp in employees: 
#     percent = attendance_percentage(emp[2]) 
#     print(f"{emp[1]} ({emp[0]}) - Attendance: {percent:.2f}%")


##########################################################

# 16. COMPUTE MARKS OF 2 STUDENTS.

# def computeAverage(list1,n): 
#     total = 0 
#     for marks in list1: 
#         total = total + marks 
#         average = total / n 
#     return average 
    
# list1 = [] 
# print("How many students marks you want to enter: ") 
# n = int(input()) 
# for i in range(0,n): 
#     print("Enter marks of student",(i+1),":") 
#     marks = int(input()) 
#     list1.append(marks) 
#     average = computeAverage(list1,n) 
# print("Average marks of",n,"students is:",average)

##########################################################

# 17. E-Commerce Product Review Analyzer. 

# products = [ 
#     ["Laptop", [5, 4, 4, 5, 5]], 
#     ["Headphones", [3, 4, 2, 3]], 
#     ["Mouse", [5, 5, 5]], 
# ] 
 
# def average_rating(ratings): 
#     return sum(ratings) / len(ratings) 


# print("Product Ratings:") 
# for product in products: 
#     print(f"{product[0]} - Avg Rating: {average_rating(product[1]):.2f}") 


# top_product = max(products, key=lambda x: sum(x[1])) 
# print(f"\nTop Rated Product: {top_product[0]} - Avg: {sum(top_product[1]):.2f}")


##################################################################

# 18. Hospital Patient Tracker. 

# patients = [ 
#     ["P101", "Rahul", ["Fever", "Cough"], True], 
#     ["P102", "Anita", ["Headache"], False], 
#     ["P103", "Sunil", ["Fever"], True], 
#     ["P104", "Divya", ["Cough", "Cold"], False], 
# ] 

 
# def admitted_patients(): 
#     return [p for p in patients if p[3]==True] 
 
# def search_symptom(symptom): 
#     return [p[1] for p in patients if symptom in p[2]] 
 
# def admitted_count(): 
#     admitted = len([p for p in patients if p[3]]) 
#     discharged = len(patients) - admitted 
#     return admitted, discharged 
 
# print("Admitted Patients:") 
# for p in admitted_patients(): 
#     print(f"{p[1]} -{p[0]}") 
 
# print("\nPatients with Fever:", search_symptom("Fever")) 
# a, d = admitted_count() 
# print(f"\nAdmitted: {a}, Discharged: {d}")


####################################################

# 19. Library Book Management System.

# library = [ 
#     ["The Alchemist", "Paulo Coelho", 1988, True], 
#     ["1984", "George Orwell", 1949, True], 
#     ["The Great Gatsby", "F. Scott Fitzgerald", 1925, False], 
# ] 
 

# def view_books(): 
#     for book in library: 
#         # status = "Available" if book[3]  else "Not Available" 
#         if book[3]==True:
#             status='available'
#         else:
#             status='not available'
#         print(f"{book[0]} by {book[1]} ({book[2]}) - {status}") 
 

# def search_author(): 
#     author = input("Enter author name: ") 
#     # found = False
#     for book in library: 
#         if author.lower() == book[1].lower(): 
#             print(f"{book[0]} ({book[2]}) - {'Available' if book[3] else 'Not Available'}") 
#             # found = True 
#         else: 
#             print("No books found by that author.") 
 
# library = [ 
#     ["The Alchemist", "Paulo Coelho", 1988, True], 
#     ["1984", "George Orwell", 1949, True], 
#     ["The Great Gatsby", "F. Scott Fitzgerald", 1925, False], 
# ] 

# def borrow_book(): 
#     title = input("Enter book title to borrow: ") 
#     for book in library: 
#         if title.lower() == book[0].lower(): 
#             if book[3]: 
#                 book[3] = False 
#                 print(f"You borrowed '{book[0]}'") 
#                 return 
#             else: 
#                 print("Book is not available") 
#                 return 
#     print("Book not found") 
 
# def return_book(): 
#     title = input("Enter book title to return: ") 
#     for book in library: 
#         if title.lower() == book[0].lower(): 
#             if not book[3]: 
#                 book[3] = True 
#                 print(f"You returned '{book[0]}'") 
#                 return 
#             else: 
#                 print("Book was already available") 
#                 return 
#     print("Book not found") 
 
# def menu(): 
#     print("\n--- Library Menu ---") 
#     print("1. View All Books") 
#     print("2. Search by Author") 
#     print("3. Borrow Book") 
#     print("4. Return Book") 
#     print("5. Exit")

# while True: 
#     menu() 

#     choice = input("Choose an option: ") 
     
#     if choice == "1": 
#         view_books() 
#     elif choice == "2": 
#         search_author() 
#     elif choice == "3": 
#         borrow_book() 
#     elif choice == "4": 
#         return_book() 
#     elif choice == "5": 
#         print("Goodbye!") 
#         break 
#     else: 
#         print("Invalid choice!")


####################################################################

# FLIGHT BOOKING SYSTEM

# flights = [ 
#     ["AI101", 2, ["Ravi"]], 
#     ["AI202", 3, []], 
# ] 
 
# def book_ticket(flight_no, passenger): 
#     for flight in flights: 
#         if flight[0] == flight_no: 
#             if len(flight[2]) < flight[1]: 
#                 flight[2].append(passenger) 
#                 return f"{passenger} booked on {flight_no}" 
#             else: 
#                 return "No seats available" 
#     return "Flight not found" 
 
# def cancel_ticket(flight_no, passenger): 
#     for flight in flights: 
#         if flight[0] == flight_no and passenger in flight[2]: 
#             flight[2].remove(passenger) 
#             return f"{passenger}'s ticket canceled on {flight_no}" 
#     return "Passenger or Flight not found" 
 
# def show_passengers(flight_no): 
#     for flight in flights: 
#         if flight[0] == flight_no: 
#             return flight[2] 
#     return "Flight not found" 
 
# print(book_ticket("AI101", "Meena")) 
# print(cancel_ticket("AI101", "Ravi")) 
# print("Passengers on AI101:", show_passengers("AI101"))

#####################################################################



# LIST MEHTODS 


# myList = [22,4,16,38,13] #myList already has 5 elements 
# choice = 0 
# while True:     
#     print("The list 'myList' has the following elements", myList) 
#     print("\nL I S T O P E R A T I O N S") 
#     print(" 1. Append an element") 
#     print(" 2. Insert an element at the desired position") 
#     print(" 3. Append a list to the given list") 
#     print(" 4. Modify an existing element") 
#     print(" 5. Delete an existing element by its position") 
#     print(" 6. Delete an existing element by its value") 
#     print(" 7. Sort the list in ascending order") 
#     print(" 8. Sort the list in descending order") 
#     print(" 9. Display the list") 
#     print(" 10. Exit") 

#     choice = int(input("ENTER YOUR CHOICE (1-10): "))


#     #  #append element 
#     if choice == 1: 
#         element = int(input("Enter the element to be appended: ")) 
#         myList.append(element)
#         print("The element has been appended\n")


#     #insert an element at desired position 
#     elif choice == 2: 
#         element = int(input("Enter the element to be inserted: ")) 
#         pos = int(input("Enter the position:")) 
#         myList.insert(pos,element) 
#         print("The element has been inserted\n") 


#     #append a list to the given list 
#     elif choice == 3: 
#         newList = eval(input( "Enter the elements separated by commas")) 
#         myList.extend(list(newList)) 
#         print("The list has been appended\n")


#     #modify an existing element
#     elif choice == 4:
#         i = int(input("Enter the position of the element to be modified: "))
#         if i < len(myList): 
#             newElement = int(input("Enter the new element: ")) 
#             oldElement = myList[i]
#             myList[i] = newElement
#             print("The element",oldElement,"has been modified\n") 
#         else: 
#             print("Position of the element is more than the length of list")


#     #delete an existing element by position 
#     elif choice == 5: 
#         i = int(input("Enter the position of the element to be deleted: ")) 
#         if i < len(myList): 
#             element = myList.pop(i) 
#             print("The element",element,"has been deleted\n") 
#         else: 
#             print("\nPosition of the element is more than the length of list")


#     #delete an existing element by value 
#     elif choice == 6: 
#         element = int(input("\nEnter the element to be deleted: ")) 
#         if element in myList: 
#             myList.remove(element) 
#             print("\nThe element",element,"has been deleted\n") 
#         else: 
#             print("\nElement",element,"is not present in the list") 


#     #list in sorted order
#     elif choice == 7: 
#         myList.sort() 
#         print("\nThe list has been sorted")


#     #list in reverse sorted order 
#     elif choice == 8: 
#         myList.sort(reverse = True) 
#         print("\nThe list has been sorted in reverse order") 


#     #display the list 
#     elif choice == 9: 
#         print("\nThe list is:", myList) 


#     #exit from the menu 
#     elif choice == 10:
#         break

#     else: 
#         print("Choice is not valid")
#         print("\n\nPress any key to continue..............") 
#         ch = input()


#############################################################################
