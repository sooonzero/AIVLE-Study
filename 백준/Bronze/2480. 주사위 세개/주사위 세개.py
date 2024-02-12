import sys

a, b, c = map(int, sys.stdin.readline().split())
d=0
result = 0

if a==b==c:
    result = 10000 + (a*1000)

elif a==b or a==c:
    result = 1000 + (a*100)

elif b==c:
    result = 1000 + (b*100)

elif a>b and a>c:
    result = a*100
elif b>a and b>c:
    result = b*100
elif c>a and c>b:
    result = c*100

else:
    result = a*100
    

print(result)



