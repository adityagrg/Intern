#program to calculate the no. of words in a file

filename = input("Enter file name : ")

f = open(filename, "r")
noofwords = 0

for line in f:
    words = line.split()
    noofwords += len(words)
f.close()
print(noofwords)