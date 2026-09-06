# Print nbrs in given sequence using FOR LOOP

a=[10,20,30,40]
for i in a:
    print(i)

###########################################################

# Print specifying odd or even numbers in sequence FOR LOOP

number=[1,2,3,4,5,6,7,8,9,10]
for i in number:
    if (i % 2) == 0:
        print(i, "is Even Number")
    else:
        print(i,"is Odd Number")

########################################################

# Range Function range([start], stop, [step])
# Start optional default (0), stop required, excluded step optional default (1)

for num in range(1, 6, 2):  # start frm 1 stop till 5 add 2 with previous output and print
    print(num)

#######################################################

# print first 5 natural numbers using WHILE LOOP

count=1
while count<=5:
    print(count)
    count+=1

#########################################################

# Break Statement: If condition satisfied breaak and out of loop

for num in range(5):
    num=num+1
    if num==4:
        break
    print("Num has value ", num)
print("Encountered break so out of Loop")

#########################################################

# Continue Statement: if condition satisfied skip that and return back to loop; skip that iteration

num=0
for num in range(6):
    num=num+1
    if num==3:
        continue
    print('num has value', num)


##########################################################

# LOOPING LIST 

list1 = [1, 10.5, 'khan']
for i in list1:
    print(i) 


# LOOPING DICTIONARY 

student = {
    "name": "Luqman",
    "age": 26,
    "isPass": True
}

for key, value in student.items():
    print(key, ":-" ,value)

#############################################################
