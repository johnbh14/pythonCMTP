filename = input("Input A Filename: ")
fh = open(filename, "r")
for line in fh:
    print(line.upper(), end = "")
