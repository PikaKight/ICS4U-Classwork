"""
diction = {
    "hello": 1,
    "hi": 2,
    "goodbye": 3,
    "bye": 4
}

word = input()

try:
    del diction[word]
except KeyError:
    print("Key {} not found".format(word))

print (diction)
"""
new = {
    "Name": {"Hello":"World", "form": "temperary"},
    "Lie": {"Cake": "Is"}
}

print(new["Name"])