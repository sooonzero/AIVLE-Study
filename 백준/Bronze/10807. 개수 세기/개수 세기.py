n = int(input())
a = list(map(int, input().split()))
b = int(input())
result = 0

for i in range (n):
    if a[i] == b:
        result += 1

print(result)


