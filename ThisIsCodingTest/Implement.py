# 예제 4-1 상하좌우

N = int(input())

data = list(map(str, input().split()))

x, y = 1, 1

cmd = [('L', (0, -1)), ('R', (0, 1)), ('U', (-1, 0)), ('D', (1, 0))]

for i in data:
  for j in cmd:
    if i == j[0]:
      x += j[1][0]
      y += j[1][1]
      if x < 1:
        x = 1
      elif x > N:
        x = N
      elif y < 1:
        y = 1
      elif y > N:
        y = N

print(x, y) 

# 예제 4-2 시각
N = int(input())

Count = 0

for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        Count += 1

print(Count)

# 예제 4-3 왕실 나이트
# 다시 풀기

# 예제 4-4 게임 개발
# 다시 풀기



