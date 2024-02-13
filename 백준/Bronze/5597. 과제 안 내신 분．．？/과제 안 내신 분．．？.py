student=[]
nstudent=[]
j = 1
for i in range(28):
    student.append(int(input()))

student.append(31)
student.append(31)
student.sort()


for i in range(30):
    if student[i] != j:
        student.insert(i, j)
        nstudent.append(j)
        j+=1
    else:
        j+=1
    

for x in nstudent:
    print(x)
