import json

"""
game = {
    "name": "PikaKight",
    "Level": 1,
    "is alive": True
}

print (game)

json_string = json.dumps(game)
print(json_string)



with open("c:/Users/PikaKight/CS_Work/ICS4U-Classwork/main_notes/File_stuff/dictionary.txt", 'w') as f:
    f.write(json_string)

with open("c:/Users/PikaKight/CS_Work/ICS4U-Classwork/main_notes/File_stuff/dictionary.json", 'w') as f:
    f.write(json_string)

"""
with open("c:/Users/PikaKight/CS_Work/ICS4U-Classwork/main_notes/File_stuff/dictionary.json", 'r') as f:
    player = json.load(f)

print (type(player))
print (player)
print(player["name"])

print()
print("Saving")
player["Level"] += 50
player["is alive"] = True
print()
print("Complete")

with open("c:/Users/PikaKight/CS_Work/ICS4U-Classwork/main_notes/File_stuff/dictionary.json", 'w') as f:
    json.dump(player, f)




