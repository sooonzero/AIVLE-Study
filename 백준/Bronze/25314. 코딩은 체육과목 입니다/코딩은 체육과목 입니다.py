n = int(input())
a = n//4
if n%4 > 0:
    a+=1
for i in range(a):
    print('long', end=' ')
print('int')
