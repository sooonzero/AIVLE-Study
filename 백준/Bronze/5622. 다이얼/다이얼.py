a = input()
result = 0
for x in a: 
    if x == 'A' or x=='B' or x=='C':
        result +=3
    elif x=='D' or x=='E' or x=='F':
        result +=4
    elif x=='G' or x=='H' or x=='I':
        result +=5
    elif x=='J' or x=='K' or x=='L':
        result +=6
    elif x=='M' or x=='N' or x=='O':
        result +=7
    elif x=='P' or x=='Q' or x=='R' or x=='S':
        result +=8
    elif x=='T' or x=='U' or x=='V':
        result +=9
    elif x=='W' or x=='X' or x=='Y' or x=='Z':
        result +=10
    else:
        result +=11



print(result)
