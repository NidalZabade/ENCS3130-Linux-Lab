import re
import os

file = input("Enter file name\n")
FileExists1 = os.path.exists(file)
if not FileExists1:
    print("There no such file\n")
    exit(0)
f = open(file, "r")
counter = 0
linecount = 0
for line in f:
    palindrome = ""
    line = line.strip()
    linecount += 1

    words = re.split(' ', line)
    for word in words:
        temp = word.lower()
        if temp == temp[::-1]:
            palindrome += word + " "
            counter += 1
        else:
            continue
    if palindrome != "":
        print("Line " + str(linecount) + ": " + palindrome)
print("Total palindromic words: " + str(counter))
