import sys
dong = list(map(int,sys.stdin.readline().split()))
right = [1,1,2,2,2,8]
answer = []

for i in range(len(dong)):
    answer.append((right[i] - dong[i]))

for x in answer:
    print(x, end=' ')
    
