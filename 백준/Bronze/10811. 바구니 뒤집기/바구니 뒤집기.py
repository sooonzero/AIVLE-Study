n, m = map(int,input().split())

a = [i for i in range(1, n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    temp = a[x-1:y]
    temp.reverse()
    a[x-1:y] = temp

for x in a:
    print(x, end=' ')