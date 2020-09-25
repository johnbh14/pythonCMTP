import sys

filename = input("Input A Filename: ")
if filename == "money makes the world go around":
    print("That's Not A File Name! That's A Song!")
    sys.exit()
fh = open(filename, "r")
for line in fh:
    print(line.upper(), end = "")
