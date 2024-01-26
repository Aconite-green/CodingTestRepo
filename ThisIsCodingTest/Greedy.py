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
arr = []

for _ in range(N):
    number = map(int, input().split())
    arr.append(number)

arr.sort()

arr_index = 0
cnt = 0

for _ in range(M):
  
  if(cnt <= K):
    result = result + arr[arr_index]
    cnt += 1
  else:
    arr_index += 1
    cnt = 0

print(result)

# 예제 3-3 숫자 카드 게임
