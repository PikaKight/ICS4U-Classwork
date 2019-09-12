def dictionary():
    d = {"apple": 4, "pears": 1} #create a diction are var = {}

    print (d["apple"]) #prints the value of apple

    d["orange"] = 5 #adds the key orange and value of 5

    print (d) #prints the dictionary

    d.pop("pears") #removes the key pears and value 

    print (d) #prints new dictionary

def student_dict():
    student = {
        "First Name:": "Frank",
        "Last Name:": "Smith",
        "Grade:": 11,
        "Homeroom:": "11G"
    }

    for key in student.keys(): #runs through the dictionary for each key

        student[key] = None #sets each key value to none

    for key in student.keys():

        if key.find("Name") > 0: #checks to see where "Name" is and check if it is great than 0
            student[key] = None
        if "Name" in key: #checks to see if "Name" is in key
            student[key] = None
        else:
            continue


    for key, value in student.items():
        print (key, value) 

def shopping():

    fruit = {
        "apples": 5,
        "pears": 2,
        "plums": 11,
        "peaches": 7
    }
           
    shopping_lis = []

    for fruit, qty in fruit.items():
        if qty <= 5:
            shopping_lis.append(fruit)
    
    print (shopping_lis)

shopping()