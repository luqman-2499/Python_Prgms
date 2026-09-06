# TEST 1

# 1. 

# def SumOfNum(num):
#     sum=0
#     for i in range(1,num+1):
#         sum+=i
#     print(sum)

# num=int(input("enter number: "))
# SumOfNum(num)



# 2. 

# string=input("enter string: ")
# cleaned=string.strip().lower()

# if cleaned==cleaned[::-1]:
#     print("String is Palindrome")
# else:
#     print("String Not Palindrome")


# 3. 

# def Count_Char(st):
#     count=0
#     for i in st:
#         if i==char:
#             count+=1
#         else:
#             pass
#     return count

# st=input("enter string: ")
# char=input("enter character to search: ")
# occur=Count_Char(st)
# print("number of times character occured: ", occur)


# 4. 

# str= input("enter string: ")
# print(str.upper())
# print(str.lower())
# print(len(str))
# print(str.title())


# str="  Lukman   Usman"
# print(str.replace('k','q'))
# print(str.strip().split())



# 5. 

# def replacevowels(st):
#     newstr=''
#     for char in st:
#         if char in 'aeiou':
#             char='*'
#             newstr+=char
#         else:
#             newstr+=char
#     return newstr


# st=input("enter string: ")
# st1=replacevowels(st)

# print("orginal string: ", st)
# print("new string: ", st1)


########### END OF TEST 1 ################


# TEST 2

# 1. 

# student=['luqman','maaz','mantesh'] 
# attendance = { 
#     'luqman':[1, 1, 1, 0, 1], 
#     'maaz':[1, 0, 1, 1, 1], 
#     'mantesh':[1, 1, 1, 0, 1] 
# } 

# for name in student:
#     days_present=sum(attendance[name])
#     percentage=(days_present/5)*100
#     print(f" {name} - presnt days: {days_present}/5 days percentage: {percentage}%")


# 2. 

# available_rooms=list(range(1,11))
# booked_rooms=[]

# def book_room(room_no):
#     if room_no in available_rooms and room_no not in booked_rooms:
#         booked_rooms.append(room_no)
#         available_rooms.remove(room_no)
#         print("Room Booked Successfully")
#     else:
#         print(f" Room {room_no} Not Available ")

# book_room(3)
# book_room(5)
# book_room(3)

# print("Available Rooms:", available_rooms)
# print("Booked Rooms", booked_rooms)


##################  END OF TEST 2 #########################


# TEST 3

# 1. 

# orders=[
#         [101,'Luqman',['shoes','shirt'],True],
#         [102,'Maaz',['Watch','shoes'],False],
#         [103,'Mantesh',['Laptop','suit'],True],
#     ]   

# def undelivered_orders():
#     return[o for o in orders if o[3]==False]

# def deliver_by_customer(name):
#     count=0
#     for o in orders:
#         if o[1].lower()==name.lower():
#             count+=len(o[2])
#     return count

# def delivered_orders(order_id):
#     for o in orders:
#         if o[0]==order_id:
#             return f"{order_id} Order Delivered"
#     return f"Order not found"

# print("Undelivered Orders:", undelivered_orders())
# print("count orders:",deliver_by_customer('luqman'))
# print("delivered orders", delivered_orders(102))


# 2. 

# patients=[
#             ['p101','Luqman',['Fever','Cough'],True],
#             ['p101','Luqman',['Pain','Fever'],False],
#             ['p101','Luqman',['Cough','Headache'],True],
#             ['p101','Luqman',['Fever','Pain'],False],
#         ]

# def admitted_patients():
#     return [p for p in patients if p[3]]

# def symptoms(name):
#     return[p[1] for p in patients if p[2]=='Fever']

# def admitted_count():
#     admitted=len([p for p in patients if p[3]])
#     discharged=len(patients)-admitted
#     return admitted, discharged

# print("\n Admitted Patients:", admitted_patients())
# print("\n Patients with Fever:", symptoms("Fever")) 
# a, d = admitted_count() 
# print("\n Number of admitted & Discahrged:", admitted_count)













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
