str=list(input())

for i in range(len(str)):
    if str[i].isupper() == True:
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()

for x in str:
    print(x, end='')