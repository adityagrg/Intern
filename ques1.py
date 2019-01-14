import math

#take input and remove whitespaces
st = input()
str = st.replace(" ", "")
length = len(str)

#compute ceil and floor
output = ""
len = len(str)
ceil = math.ceil(math.sqrt(len))
floor = math.floor(math.sqrt(len))

#processing as required and giving output
i = 0
j = 0
ind = []
while(i < ceil):
    index = i
    while(j <= floor):
        if(index < length):
            ind.append(index)
            output += str[index]
        index = index+ceil
        j = j+1
    j = 0
    output += " "
    i = i+1
print(output)