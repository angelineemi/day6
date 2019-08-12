def mygen(n):
    for i in range(n):
        if i%7==0 or i%5==0:
            yield i
g=mygen(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
        
