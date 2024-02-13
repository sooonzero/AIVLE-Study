x = int(input())

score = list(map(int, input().split()))

temp = max(score)

for i in range(len(score)):
        score[i]=(score[i]/temp)*100

print(sum(score)/x)