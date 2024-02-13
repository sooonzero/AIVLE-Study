#리스트를 만들고 입력받은값을 제거 후 출력하는 방법
students = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    students.remove(applied) #소거

print(min(students))
print(max(students))
