# # 1. Storing GPS Coordinates (Immutable Location Data)

# location = ("Bangalore", 12.9716, 77.5946)  # Tuple to store city and coordinates
# print(f"City: {location[0]}, Latitude: {location[1]}, Longitude: {location[2]}")


############################################################################################


# # 2. Storing Student Information

# student = ("A123", "Meena", "Computer Science")  # Tuple for student details
# print(f"ID: {student[0]}, Name: {student[1]}, Course: {student[2]}")


#############################################################################################


# # 3. Return Multiple Values from a Function

# def get_student_details():
#     return ("Ravi", 21, "BCA")  # Returns a tuple with name, age, course

# name, age, course = get_student_details()  # Tuple unpacking
# print(name, age, course)


############################################################################################


# # 4. List of Employees with Designation

# employees = [("Ram", "Manager"), ("Sita", "Clerk"), ("John", "HR")]  # List of tuples
# for name, role in employees:
#     print(f"{name} works as a {role}")


############################################################################################


# # 5. Using Tuples as Dictionary Keys

# weather_data = {
#     ("Bangalore", "2025-06-20"): "Rainy",
#     ("Delhi", "2025-06-20"): "Sunny"
# }

# print(weather_data[("Bangalore", "2025-06-20")])  # Access using tuple key


############################################################################################

# # 6. Unpacking Tuple in Loops

# products = [("Mouse", 400), ("Keyboard", 1200), ("Monitor", 7000)]
# for product, price in products:
#     print(f"{product} costs ₹{price}")


############################################################################################

# # 7. Flight Booking Details

# flight = ("Indigo", "6E123", "Bangalore", "Mumbai", "6:00 AM")
# print(f"Flight: {flight[0]} {flight[1]} from {flight[2]} to {flight[3]} at {flight[4]}")


############################################################################################


# # 8. Storing Color Codes (Immutable RGB Values)

# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# print(f"Red color RGB: {red}")


############################################################################################

# # 9. Immutable Configuration Settings

# settings = ("Dark Mode", True, "English")
# print(f"Theme: {settings[0]}, Enabled: {settings[1]}, Language: {settings[2]}")


############################################################################################

# # 10. Bank Transaction History

# transactions = [
#     ("Deposit", 5000),
#     ("Withdrawal", 1200),
#     ("Deposit", 2000)
# ]

# for txn_type, amount in transactions:
#     print(f"{txn_type} of ₹{amount}")


############################################################################################

# # 11. GPS Coordinates in a Delivery App

# delivery_points = [
#     ("Customer A", (12.9611, 77.6387)),
#     ("Customer B", (13.0352, 77.5970))
# ]

# def show_delivery_locations():
#     for name, (lat, lon) in delivery_points:
#         print(f"{name} → Latitude: {lat}, Longitude: {lon}")
# show_delivery_locations()


############################################################################################

# # 12. Student Info System (Immutable Records)

# students = [
#     ("S001", "Arjun", "BCA"),
#     ("S002", "Megha", "B.Sc"),
#     ("S003", "Ravi", "B.Com")
# ]

# def get_student(id):
#     for student in students:
#         if student[0] == id:
#             return student
#     return None
# print(get_student("S002"))


#########################################################################################


# # 13. Return Multiple Values in Invoice System

# def create_invoice(product, qty, price):
#     total = qty * price
#     return (product, qty, price, total)

# item = create_invoice("Mouse", 2, 400)
# print(f"Product: {item[0]}, Qty: {item[1]}, Unit Price: {item[2]}, Total: ₹{item[3]}")


##################################################################################################


# # 14. Employee Directory with Search Feature
# employees = [
#     ("E101", "Priya", "HR"),
#     ("E102", "Vikram", "Sales"),
#     ("E103", "Neha", "IT")
# ]

# def search_by_department(dept):
#     return [emp for emp in employees if emp[2] == dept]
# print(search_by_department("Sales"))


#######################################################################################################

# # 15. Weather Forecasting Using Tuple Keys

# weather_data = {
#     ("Bangalore", "2025-06-20"): "Rainy",
#     ("Mumbai", "2025-06-20"): "Cloudy"
# }

# def get_forecast(city, date):
#     return weather_data.get((city, date), "No Data")
# print(get_forecast("Bangalore", "2025-06-20"))


############################################################################################


# # 16. E-Commerce Product List

# products = [
#     ("P101", "Laptop", 65000),
#     ("P102", "Tablet", 23000),
#     ("P103", "Monitor", 11000)
# ]

# def show_products():
#     for pid, name, price in products:
#         print(f"{pid}: {name} → ₹{price}")

# show_products()

############################################################################################


# # 17. Airline Reservation Summary

# flights = [
#     ("6E101", "Indigo", "Bangalore", "Delhi", "10:30 AM"),
#     ("AI202", "Air India", "Mumbai", "Chennai", "1:45 PM")
# ]

# def show_flight_details():
#     for flight in flights:
#         print(f"Flight {flight[0]} ({flight[1]}) from {flight[2]} to {flight[3]} at {flight[4]}")

# show_flight_details()


############################################################################################


# # 18. Color Picker for Web App Design

# color_palette = {
#     "Primary": (255, 99, 71),
#     "Secondary": (60, 179, 113),
#     "Accent": (100, 149, 237)
# }

# def display_colors():
#     for name, rgb in color_palette.items():
#         print(f"{name} Color RGB: {rgb}")

# display_colors()


############################################################################################


# # 19. App Settings Configuration

# settings = ("Dark Mode", True, "English", "v1.0.5")

# def print_settings():
#     print(f"Theme: {settings[0]}, Enabled: {settings[1]}, Language: {settings[2]}, Version: {settings[3]}")

# print_settings()


###################################################################################################


# # 20. Mini Bank Transaction Logger

# transactions = [
#     ("2025-06-19", "Deposit", 10000),
#     ("2025-06-20", "Withdrawal", 2500),
#     ("2025-06-20", "Deposit", 5000)
# ]

# def print_statement():
#     balance = 0
#     print("Date\t\tType\t\tAmount\tBalance")
#     for date, t_type, amount in transactions:
#         balance += amount if t_type == "Deposit" else -amount
#         print(f"{date}\t{t_type}\t₹{amount}\t₹{balance}")

# print_statement()


###################################################################################################


# # 21. University Course Management System

# courses = [
#     ("CS101", "Python Programming", 4, "Semester 1"),
#     ("CS201", "Data Structures", 4, "Semester 2"),
#     ("CS301", "Databases", 3, "Semester 3")
# ]

# enrollments = [
#     ("S001", "Arjun", ["CS101", "CS201"]),
#     ("S002", "Megha", ["CS101", "CS301"])
# ]
# def print_student_courses():
#     for student_id, name, course_list in enrollments:
#         print(f"{name} enrolled in:")
#         for c_code in course_list:
#             course = next((c for c in courses if c[0] == c_code), None)
#             if course:
#                 print(f" - {course[1]} ({course[0]})")

# print_student_courses()


###################################################################################################


# # 22. Smart City Traffic Light Monitoring

# traffic_lights = [
#     (101, "MG Road", "Red"),
#     (102, "Brigade Road", "Green"),
#     (103, "Majestic", "Yellow")
# ]

# change_logs = [
#     ("2025-06-20 09:01", 101, "Green", "Red"),
#     ("2025-06-20 09:05", 102, "Red", "Green")
# ]

# def print_light_logs():
#     for log in change_logs:
#         print(f"Time: {log[0]}, Intersection {log[1]} changed from {log[2]} to {log[3]}")

# print_light_logs()


###################################################################################################


# # 23. Hospital Patient Visit Record System

# visit_history = [
#     ("P001", "2025-06-01", "Dr. Anil", "Fever", "Paracetamol"),
#     ("P002", "2025-06-03", "Dr. Smith", "Back Pain", "Ibuprofen"),
#     ("P001", "2025-06-10", "Dr. Anil", "Cold", "Cetrizine")
# ]

# def show_patient_visits(pid):
#     print(f"Visit history for patient {pid}:")
#     for visit in visit_history:
#         if visit[0] == pid:
#             print(f"Date: {visit[1]}, Doctor: {visit[2]}, Issue: {visit[3]}, Meds: {visit[4]}")

# show_patient_visits("P001")


###################################################################################################


# # 24. Travel Agency Tour Booking System

# tour_packages = [
#     ("T001", "Goa", 12000, "3 Days"),
#     ("T002", "Manali", 18000, "5 Days"),
#     ("T003", "Kerala", 15000, "4 Days")
# ]

# bookings = [
#     ("B001", "Customer A", "T001", "2025-07-01"),
#     ("B002", "Customer B", "T003", "2025-08-15")
# ]

# def print_booking_details():
#     for bid, cname, tid, date in bookings:
#         tour = next((t for t in tour_packages if t[0] == tid), None)
#         print(f"{cname} booked {tour[1]} ({tid}) on {date} for ₹{tour[2]}")

# print_booking_details()


###################################################################################################


# # 25. Expense Tracker with Audit Log

# expenses = [
#     ("2025-06-01", "Groceries", 1500, "Cash", "Monthly shopping"),
#     ("2025-06-02", "Petrol", 1000, "Card", "Fuel for car"),
#     ("2025-06-03", "Dining", 750, "UPI", "Dinner out")
# ]

# def total_spent():
#     return sum(e[2] for e in expenses)

# def filter_by_mode(mode):
#     return [e for e in expenses if e[3] == mode]

# print("Total spent:", total_spent())
# print("UPI Transactions:", filter_by_mode("UPI"))


###################################################################################################


# # 26. Quiz Game App

questions = [
    ("Capital of India?", "Delhi", "Mumbai", "Chennai", "Delhi"),
    ("Largest planet?", "Mars", "Earth", "Jupiter", "Jupiter")
]

def play_quiz():
    score = 0
    for q, a, b, c, correct in questions:
        print(f"{q}\nA. {a}\nB. {b}\nC. {c}")
        ans = input("Your answer: ")
        if ans.strip().lower() == correct.lower():
            score += 1
    print(f"Your Score: {score}/{len(questions)}")

play_quiz()


################################### END OF TUPLES  #############################################