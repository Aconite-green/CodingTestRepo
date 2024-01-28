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
userInput = input()
row = int(userInput[1])
column = int(ord(userInput[1]) - ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0

for step in steps:
  nextRow = row + step[0]
  nextCol = column + step[1]
  if(nextRow >= 1 and nextRow <= 8 and nextCol >= 1 and nextCol <= 8):
    count +=1

print(count)

# 예제 4-4 게임 개발
N, M = map(int, input().split())

x,y,direction = map(int, input().split())

gameMap = []
for _ in range(N):
  gameMap.append(list(map(int, input().split())))


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

graph = [[0] * M for _ in range(N)]

def turnLeft():
  global direction
  direction -=1
  if direction == -1:
    direction = 3

count = 1
turnTime = 0

while True:
  turnLeft()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if graph[nx][ny] == 0 and gameMap[nx][ny] == 0:
    x = nx
    y = ny
    graph[x][y] = 1
    count += 1
    turnTime = 0
  else:
    turnTime +=1
  if turnTime == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if gameMap[nx][ny] == 0:
      x = nx
      y = ny
      turnTime = 0
    else:
      break
   

print(count)



