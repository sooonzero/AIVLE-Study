a, b = map(int, input().split())
balls = [0]*a
for i in range (b):
    x, y, z = map(int,input().split())
    for j in range(x-1,y):
        balls[j]=z

for k in balls:
    print(k, end=' ')
