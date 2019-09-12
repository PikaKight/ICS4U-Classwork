d = {"apple": 4, "pears": 1} #create a diction are var = {}

print (d["apple"]) #prints the value of apple

d["orange"] = 5 #adds the key orange and value of 5

print (d) #prints the dictionary

d.pop("pears") #removes the key pears and value 

print (d) #prints new dictionary

student = {
    "First_Name": "Frank",
    "Last_Name": "Smith",
    "grade": 11,
    "Homeroom": "11G"
}

for key, value in student.items():
    print(key, value)