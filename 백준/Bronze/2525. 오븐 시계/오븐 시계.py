A, B = map(int, input().split())
C = int(input())

hour = C//60
min = C%60

A += hour
B += min

if(B > 59):
    
    A +=(B//60)
    B=B % 60

if(A > 23):
    A=A%24

print(f"{A} {B}")