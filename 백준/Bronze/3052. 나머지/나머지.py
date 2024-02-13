number=set()

for _ in range(10):
    x = int(input())
    number.add(x%42)

print(len(number))