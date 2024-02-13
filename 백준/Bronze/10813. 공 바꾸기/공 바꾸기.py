n, m = map(int, input().split())

number = [i for i in range (1, n+1)]
x = 0
for i in range(m):
    a, b = map(int,input().split())
    a-=1
    b-=1
    x = number[b]
    number[b] = number[a]
    number[a] = x

for j in number:
    print(j, end =' ')
