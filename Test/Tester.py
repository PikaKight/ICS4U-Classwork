# Student = dict() # creates an empty dictionary

# start = True

# while start:
    
#     F_name = input("Student First Name: ")
#     L_name = input ("Stuendt Last Name: ")
    
#     Student[F_name] = L_name

#     print (Student[F_name]) #returns the value

#     ask = input("Do you want to continue (Y/N)")

#     if ask == "Y":
#         continue
#     else: 
#         start = False

# print (Student) #returns the dictionary 
# while True:
#     try:
#         num = int(input("Enter a number: "))
#     except ValueError:
#         print("OOPS. Cant convert that to int.")
#     else:
#         break

# result = num * 2
# print(f"{num} * 2 = {result}")
student_list = {
    "Marcus": {
        "Marks": [100, 100, 100]
    }
}
marks = student_list["Marcus"]["Marks"]
print (marks)
new_marks = int(input("Enter new Marks:"))
marks.append(new_marks)
marks.sort()
print(student_list) 
