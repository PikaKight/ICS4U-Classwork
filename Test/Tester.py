Student = dict()

start = True

while start:
    
    F_name = input("Student First Name: ")
    L_name = input ("Stuendt Last Name: ")
    
    Student[F_name] = L_name

    ask = input("Do you want to continue (Y/N) ")

    if ask == "Y":
        continue
    else: 
        start = False

print (Student)