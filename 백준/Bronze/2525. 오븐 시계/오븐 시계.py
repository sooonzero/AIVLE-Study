import sys

a, b = map(int, sys.stdin.readline().split())
c = int(input())

b += c

if b>=60:
    a += b//60
    b %= 60

if a>23:
    a -= 24

if a==24:
    a=0

print(a, b)


