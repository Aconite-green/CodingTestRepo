sing_line = list(map(int, input().split()))

if sing_line == list(range(1, 9)):
    print("ascending")
elif sing_line == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")



