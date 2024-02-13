n = int(input())
for i in range(n):
    a, b = input().split()
    for x in b:
        print(x *int(a), end='')
    print()
