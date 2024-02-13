a, b = list(input().split())
a= list(reversed(a))
b= list(reversed(b))
a = "".join(a)
b = "".join(b)
result=[]
result.append(a)
result.append(b)
print(max(result))
