a = [1,0,1,0,2,0,0,3,65]
b = [i for i, e in enumerate(a) if e != 0]
print(b)

a = a + b
print(a)