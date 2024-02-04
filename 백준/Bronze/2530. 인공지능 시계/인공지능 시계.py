A, B, C = map(int, input().split())
D = int(input())

hour = D//3600
D = D%3600
min = D//60
D = D%60
sec = D

A += hour
B += min
C += sec

if(C > 59):
    B += (C//60)
    C = C%60

if(B > 59):
    
    A +=(B//60)
    B=B % 60

if(A > 23):
    A=A%24

print(f"{A} {B} {C}")