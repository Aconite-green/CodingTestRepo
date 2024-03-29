
import sys

# 입력 부분
N, M = map(int, input().split())
N_array = list(map(int, sys.stdin.readline().split()))

# 누적 합 배열을 구성
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1] + N_array[i])

# 쿼리 처리
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    # 구간 합을 누적 합을 이용하여 계산
    print(prefix_sum[end] - prefix_sum[start-1])
