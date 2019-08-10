string=str(input("Enter a string: "))
frequency = {}
for i in string:
    if i in frequency: 
        frequency[i] += 1
    else: 
        frequency[i] = 1
print ("Count of all characters in the string is :"+  str(frequency))

