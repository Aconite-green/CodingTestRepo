import sys


while True:
    sides = list(map(int, sys.stdin.readline().split()))
    sides.sort()
    if sides[0] ==0 and sides[1]==0 and sides[2] ==0:
        break
    elif sides[2]**2 == sides[1]**2+sides[0]**2:
        print("right")
    else:
        print("wrong")