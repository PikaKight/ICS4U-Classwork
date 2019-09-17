
with open("file.txt", "r") as f:
    for line in f:
        if line.startswith("N"):
           print (line.strip())
        #print (line)