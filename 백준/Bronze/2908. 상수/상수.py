a,b = input().split()
result = []
a= int(a[::-1])
b= int(b[::-1])
result.append(a)
result.append(b)

print(max(result))
