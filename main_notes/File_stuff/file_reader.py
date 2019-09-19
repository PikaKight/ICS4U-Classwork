import os

with open("c:/Users/PikaKight/CS_Work/ICS4U-Classwork/main_notes_file stuff/file.txt", "r") as f:
    for line in f:
        if line.startswith("N"):
           print (line.strip())
        #print (line)