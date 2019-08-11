n=int(input("enter the size of a: "))
m=int(input("enter the size of b: "))
a=[]
for x in range(n):
    x=int(input("enter the array elements of a: "))
    a.append(x)
b=[]
for y in range(m):
    y=int(input("enter the array elements of b: "))
    b.append(y)
set1=set(a)
set2=set(b)
if set1.issubset(set2):
    print("YES")
else:
    print("NO")
