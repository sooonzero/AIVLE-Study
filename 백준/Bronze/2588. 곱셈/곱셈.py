a = int(input())
b = int(input())
q = b
x = b//100
y = (b - (x*100))//10
z = (b - (x*100) - (y*10))

print(a * z)
print(a * y)
print(a * x)
print(a * q)