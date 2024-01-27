# 예제 3-1 거스름돈
N = int(input())

coin_types = [500, 100, 50, 10]
change = 0

for coin in coin_types:
  change += N // coin
  N %= coin

print(change)

# 예제 3-2 큰수의 법칙 (수정 필요)
N,M,K = map(int, input().split())
result = 0

arr = list(map(int, input().split()))
arr.sort()

first = arr[N-1]
second = arr[N-2]

while True:
  for _ in range(K):
    if M==0:
      break
    result += first
    M -= 1
  if M==0:
    break
  result += second


print(result)

# 예제 3-3 숫자 카드 게임
N, M = map(int, input().split())


cards = [[0] * M for _ in range(N)]
minimum = [0] * N

for i in range(N):
    cards[i] = list(map(int, input().split()))
    minimum[i] = min(cards[i])

    
print(max(minimum))

# 예제 3-4 1이 될 때까지
N, K = map(int, input().split())

Count = 0

while N != 1:
  if N % K == 0:
    N = N // K
    Count += 1
  else:
    N -=1
    Count +=1

print(Count)