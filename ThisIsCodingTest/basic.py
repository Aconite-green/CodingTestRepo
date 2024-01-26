# List Comprehension
array = [i for i in range(20) if i % 2 == 1]

m,n = 1
doubleArray = [[0] * m for _ in range(n)]

# I/O

n = int(input())

data = list(map(int, input().split()))

# if there are many input
import sys
sys.stdin.readline().rstrip()