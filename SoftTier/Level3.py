################################### 평균
def calculate_and_print_average_scores_from_input():
    # 첫 번째 줄 입력: 학생 수 N과 구간 수 K
    N, K = map(int, input().split())

    # 두 번째 줄 입력: 학생들의 성적
    scores = list(map(int, input().split()))

    # 각 구간에 대한 평균 계산 및 출력
    for _ in range(K):
        a, b = map(int, input().split())
        # 인덱스 조정
        a -= 1
        b -= 1

        # 구간의 성적 합계와 평균 계산
        sum_scores = sum(scores[a:b+1])
        average = sum_scores / (b - a + 1)

        # 소수 셋째자리에서 반올림하여 출력
        print(f"{average:.2f}")

# 입력 예제에 대한 실행 예시
# calculate_and_print_average_scores_from_input()
        
########################################### 최대 수열
def longest_increasing_subsequence_input():
    # 돌의 개수 입력 받기
    N = int(input())

    # 돌의 높이 입력 받기
    stones = list(map(int, input().split()))

    # 각 돌에 대해 LIS 길이를 저장할 배열 초기화
    lis = [1] * N

    # 모든 돌에 대해 LIS 길이 계산
    for i in range(1, N):
        for j in range(i):
            if stones[i] > stones[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # 가장 긴 LIS 길이 반환 및 출력
    return max(lis)

# 입력 예제에 대한 실행 예시
# max_stones = longest_increasing_subsequence_input()
# print(max_stones)

########################################### 바이러스

def calculate_virus_count(K, P, N):
    MOD = 1000000007
    # 0.1초당 P배 증가하므로, N초 후에는 P^(N*10) 배 증가
    # 모듈러 거듭제곱을 사용하여 계산
    final_count = K
    exponent = N * 10

    while exponent > 0:
        if exponent % 2 == 1:
            final_count = (final_count * P) % MOD
        P = (P * P) % MOD
        exponent //= 2

    return final_count

# 입력 받기
K, P, N = map(int, input().split())

# 최종 바이러스 개수 계산
final_virus_count = calculate_virus_count(K, P, N)
print(final_virus_count)

########################################### 강의실 배정
def max_lectures(lectures):
    # 강의를 종료 시간 기준으로 정렬
    lectures.sort(key=lambda x: x[1])

    # 첫 강의 선택
    last = 0
    count = 0

    for start, end in lectures:
        # 이전에 선택한 강의가 끝난 후 시작하는 강의 선택
        if start >= last:
            count += 1
            last = end

    return count

# 입력 받기
N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]

# 최대 강의 수 계산
max_lectures_count = max_lectures(lectures)
print(max_lectures_count)

        
########################################### 우물안 개구리
def count_best_members_input():
    # 입력 받기: 회원 수 N과 친분 관계 수 M
    N, M = map(int, input().split())

    # 입력 받기: 회원별 역기 무게
    weights = list(map(int, input().split()))

    # 입력 받기: 친분 관계
    friendships = [tuple(map(int, input().split())) for _ in range(M)]

    # 각 회원과 친분 관계가 있는 회원의 최대 역기 무게를 저장하는 배열 초기화
    max_weight_in_friendship = [0] * (N + 1)

    # 친분 관계를 바탕으로 최대 역기 무게 갱신
    for a, b in friendships:
        max_weight_in_friendship[a] = max(max_weight_in_friendship[a], weights[b-1])
        max_weight_in_friendship[b] = max(max_weight_in_friendship[b], weights[a-1])

    # 자신이 최고라고 생각하는 회원 수 계산
    count = 0
    for i in range(1, N + 1):
        # 자신의 역기 무게가 친분 그룹 내 최대 무게보다 크거나, 친분이 없는 경우
        if weights[i-1] > max_weight_in_friendship[i] or max_weight_in_friendship[i] == 0:
            count += 1

    return count

########################################### 조립라인
def fastest_assembly_time(N, times):
    # 초기화: 첫 번째 작업장의 작업 시간
    time_A = times[0][0]
    time_B = times[0][1]

    # 각 작업장을 순회하며 최소 시간 계산
    for i in range(1, N - 1):
        next_time_A = min(time_A + times[i][0], time_B + times[i][2] + times[i][0])
        next_time_B = min(time_B + times[i][1], time_A + times[i][3] + times[i][1])

        time_A, time_B = next_time_A, next_time_B

    # 마지막 작업장의 시간 추가
    time_A += times[-1][0]
    time_B += times[-1][1]

    # 두 라인 중 최소 시간 반환
    return min(time_A, time_B)

# 입력 받기
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

# 가장 빠른 조립시간 계산
fastest_time = fastest_assembly_time(N, times)
print(fastest_time)

########################################### 동계테스트 시험예측
import sys
from collections import deque

def bfs():
    queue = deque([[0,0]])  # 얼음의 가장자리 지점은 얼음이 존재하지 않으므로 0,0 부터 시작
    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()
        
        for i in range(4): # 현재위치에서 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < N and 0 <= nx < M: 
                if ice_land[ny][nx]: #  탐색하는 곳이 얼음이라면
                    visited[ny][nx] += 1 # 방문횟수 1 증가

                elif visited[ny][nx] == 0: # 탐색하는 곳이 얼음이 아니라면
                    queue.append([ny,nx]) # 그 지점도 탐색을 해야하므로 queue에 다시 넣어준다
                    visited[ny][nx] = 1 # 방문횟수를 1로 초기화

    for y in range(N):
        for x in range(M):
            if visited[y][x] >= 2: #  방문횟수가 2이상인 곳은 얼음이 2번이상 외부 공기와 접촉한 곳이므로 녹음
                ice_land[y][x] = 0


N, M = map(int, sys.stdin.readline().split())
ice_land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상하좌우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

while True: # ice_land 안에 얼음이 존재하지 않을 때 까지 시도
    if ice_land.count([0] * M) == N: 
        break

    visited = [[0] * M for _ in range(N)] # bfs()가 시도되기 전에 계속 방문 횟수를 계속 초기화 해줘야 한다
    bfs()
    cnt += 1
        
print(cnt)
