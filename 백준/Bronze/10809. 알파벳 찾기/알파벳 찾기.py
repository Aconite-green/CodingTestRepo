import sys

S = sys.stdin.readline().strip()

arr = [-1] * 26

for i in range(len(S)):
    which_num =  ord(S[i]) % ord('a')
    if arr[which_num] == -1:
        arr[which_num] = i


print(*arr)
