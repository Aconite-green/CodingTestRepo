import sys

T = int(input())

for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    idx=0
    while True:
        for _ in range(int(R)):
            print(S[idx], end="")
        idx +=1
        if idx >= len(S):
            break
    print("")